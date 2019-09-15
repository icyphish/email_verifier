# Email Verifier - Checks if an email address is valid
# Mailbox Layer API key: 09e8c6f316dd2516908caaeee914ffd0
import tkinter as tk
import requests
from PIL import ImageTk
from urllib.request import urlopen

#Main Window
root = tk.Tk()
root.title(" - Email Verifier - ")
windows_height = 400
windows_width = 600
canvas = tk.Canvas(root, height=windows_height, width=windows_width)
canvas.pack()

#Get image from URL
background_imgurl = 'https://agentbox.com.au/wp-content/uploads/2017/12/about-us-3.jpg'
background_image = open('image.png', 'wb')
background_image.write(urlopen(background_imgurl).read())
background_image.close()
background_image = ImageTk.PhotoImage(file ='image.png')
canvas.create_image(1, 1, image = background_image, anchor ='n')
bg_label = tk.Label(root, image=background_image)
bg_label.place(relwidth =1, relheight=1)

#FRAME
top_frame= tk.Frame(root, bg='blue', bd=5)
top_frame.place(relx=0.5, rely=0.15, relwidth=0.85, relheight=0.1, anchor='n')

lower_frame = tk.Frame(root, bg='green',bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.85, relheight=0.6, anchor='n')

#BUTTON

button = tk.Button(top_frame, text='Verify Email:', bg='yellow', fg='red', font=('Courier',10), command=lambda: validate_email(entry.get()))
button.place(relwidth=0.3,relheight=1)

entry = tk.Entry(top_frame, bg='pink',font=('Courier',10))
entry.place(relx=0.35, relheight=1, relwidth=0.65)

label = tk.Label(lower_frame, bg='yellow',font=('Courier',14), anchor='nw', justify='left', bd=3)
label.place(relwidth=1,relheight=1)

#API Call - Validate Email
def validate_email(email_address):
    api_key= '09e8c6f316dd2516908caaeee914ffd0'
    url = 'https://apilayer.net/api/check'
    parameter = {'access_key': api_key, 'email': email_address}
    response = requests.get(url, params=parameter)
    verify_email = response.json()
    print(response.url)
    print(verify_email)

    label['text'] = response_template(verify_email)

#Sample Response
# {'email': 'icywindy@gmail.com', 'did_you_mean': '', 'user': 'icywindy', 'domain': 'gmail.com', 'format_valid': True,
#  'mx_found': True, 'smtp_check': True, 'catch_all': None, 'role': False, 'disposable': False, 'free': True, 'score': 0.8}

def response_template(verify_email):
    try:
        address_check = (verify_email['email'])
        format_check = (verify_email['format_valid'])
        mx_check = (verify_email['mx_found'])
        smtp_check = (verify_email['smtp_check'])
        score_check = (verify_email['score']*100)

        output= f"Email: \t\t\t{address_check}\nValid Format: \t\t{format_check}\nMX Found: \t\t{mx_check}" \
                f"\nSMTP Found: \t\t{smtp_check} \nReliability(0-100%): \t{score_check}%"
    except:
        output= f"""There was an error retrieving data from the server."""
    return output

#Run the program
root.mainloop()
