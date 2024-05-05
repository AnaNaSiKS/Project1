import myform_mail
import unittest


mails_correct = ["testMail1@mail.ru",
                 "user37717@st.guap.ru",
                 "sadas@gmail.com"]
mails_uncorrect = ["",
                   " ",
                   "2",
                   "sad@"
                   "asd",
                   "@gmail.com",
                   "sadsd @ asd.sd",
                   "@.ru",
                   "asdsd@mail"]

class MailTest(unittest.TestCase):
    def test_T_mail(self):
        for mail in mails_correct:
            self.assertTrue(myform_mail.check_mail(mail))
    def test_F_mail(self):
        for mail in mails_uncorrect:
            self.assertFalse(myform_mail.check_mail(mail))


if __name__ == '__main__':
    unittest.main()