from django.shortcuts import redirect
from django.views.generic import FormView
from demos.forms import FormEmailSend
from django.core.mail import send_mail, EmailMessage

class ViewSendEmail(FormView):
    form_class = FormEmailSend
    template_name = 'email_send.html'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']
        to_email = form.cleaned_data['to_email']
        emails = []
        if ',' in to_email:  # if we have multiple emails separated by commas then add them in the list
            for email in to_email.split(','):
                emails.append(email)
        else:  # if we just have a single email then add it in the list
            emails.append(to_email)

        if 'send_mail' in self.request.POST:
            send_mail_example(subject, message, from_email, emails)
        else:
            send_email_message(subject, message, from_email, emails)
        return redirect("demos-email-simple")

def send_email_message(subject, message, from_email, emails):
    email = EmailMessage(subject, message, from_email, to=emails)
    email.send()

def send_mail_example(subject, message, from_email, emails):
    send_mail(subject, message, from_email, emails)
