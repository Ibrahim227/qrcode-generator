import qrcode


first_name = str(input("Enter your First Name: "))   # Ask the user's first name
last_name = str(input("Enter your Last Name: "))    # Ask for user's last name
user_id = input("Enter your ID: ")                  # Ask dor user's ID
status = str(input("Enter your status: "))          # Ask for user's Status : Jobless or professional

# QRcode
codqr = qrcode.QRCode(version=1, box_size=10, border=4)
codqr.add_data(f"First Name: {first_name}, Last Name: {last_name}, ID: {user_id}, status: {status}")
codqr.make(fit=True)

# qr image generator
img = codqr.make_image(fill_color='black', back_color='white')
img.save(f"{first_name} {last_name}.png")
