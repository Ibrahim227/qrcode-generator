import qrcode


first_name = str(input("Enter your first_name: "))   # Ask the user's first name
last_name = str(input("Enter your last_name: "))    # Ask for user's last name
user_id = input("Enter your ID: ")                  # Ask dor user's ID
status = str(input("Enter your status: "))          # Ask for user's Status : Jobless or professional


codqr = qrcode.QRCode(version=1, box_size=10, border=4)
codqr.add_data(f"first_name:{first_name}, last_name: {last_name}, ID: {user_id}, status: {status}")
codqr.make(fit=True)

img = codqr.make_image(fill_color='black', back_color='white')
img.save(f"{first_name} {last_name}")
