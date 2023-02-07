from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse
import xlrd

from whatsapp.helpers import SendWhatsAppMessage
from whatsapp.config import CONTACTS_CSV


class SendMessageAPI(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        excel_file = request.FILES.get("excel_file")
        message = request.data.get('message')
        person = request.data.get('person')        

        if excel_file is not None and message is not None:
            suffixes = (".csv", ".xlsx", ".xls")
            if not excel_file.name.endswith(suffixes):
                return Response(
                    {"message": "Invalid File"}, status=status.HTTP_400_BAD_REQUEST
                )
            book = xlrd.open_workbook(file_contents=excel_file.read())
            worksheet = book.sheets()[0]

            send_whtsapp_msgs = SendWhatsAppMessage()
            send_whtsapp_msgs.send_message(worksheet, message)
        
        elif message is not None and person is not None:
            send_whtsapp_msgs = SendWhatsAppMessage()
            send_whtsapp_msgs.send_msg_to_individual(person, message)
        return Response(
            {"message": "success"}, status=status.HTTP_200_OK
        )


class ContactsTemplateDownload(generics.ListAPIView):

    def get(self, request):
        """
        Method to handle the get request
        """
        try:
            file_name = "contacts.csv"
            document = open(CONTACTS_CSV, "rb")
            response = HttpResponse(
                document, content_type="application/vnd.ms-excel")
            response["Content-Disposition"] = 'attachment; filename="%s"' % file_name
            return response
        except Exception as e:
            return HttpResponse(str(e))
