# Import required libraries
import tkinter as tk
from tkinter import messagebox, scrolledtext
import openai
import smtplib
# Set OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Function to generate an email based on a prompt using OpenAI's API
def generate_email(prompt):
    if not prompt:
        messagebox.showerror("Error", "Please enter a prompt.")
        return

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        generated_text = response.choices[0].text.strip()
        response_text_area.config(state=tk.NORMAL)
        response_text_area.delete('1.0', tk.END)
        response_text_area.insert(tk.END, generated_text)
        return generated_text
    except openai.error.OpenAIError as e:
        response_text_area.delete('1.0', tk.END)
        response_text_area.insert(tk.END, f"API Error: {str(e)}")
    except Exception as e:
        response_text_area.delete('1.0', tk.END)
        response_text_area.insert(tk.END, f"An unexpected error occurred: {str(e)}")

# Function to send the generated email
def send_email(recipient_email, subject, email_text):
    email = "yatikashukla31@gmail.com"
    smtp_password = "nmfi qwzw eqyn tnhi"  # SMTP Password
    smtp_server = "smtp.gmail.com"
    
    text = f"Subject: {subject}\n\n{email_text}"
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(email, smtp_password)
    server.sendmail(email, recipient_email, text)
    server.quit()

    messagebox.showinfo("Email Sent", f"Email has been sent to {recipient_email}")
# Function to handle generating email in the GUI
def generate_email_gui():
    input_text = prompt_entry.get()
    if not input_text:
        messagebox.showerror("Error", "Please enter a prompt.")
        return
    generated_email = generate_email(input_text)
    return generated_email

# Function to handle sending email through the GUI
def send_email_gui():
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    if not recipient_email or not subject:
        messagebox.showerror("Error", "Recipient email and subject are required.")
        return
    generated_email_text = generate_email_gui()
    if generated_email_text:
        send_email(recipient_email, subject, generated_email_text)

# UI
# Create the main window (root) for the Tkinter GUI
root = tk.Tk()
root.title("AI Response Generator")
root.configure(background='#f0f0f0')

# Frame for the entire GUI
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(padx=10, pady=10)

# Heading Label
heading_label = tk.Label(frame, text="AI Response Generator", bg='#f0f0f0', font=("Helvetica", 24, "bold"), fg="#333333")
heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

# Prompt Label and Entry field
prompt_label = tk.Label(frame, text="Enter your prompt for the email:", bg='#f0f0f0', font=("Helvetica", 12), fg="#333333")
prompt_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
prompt_entry = tk.Entry(frame, width=50, font=("Helvetica", 12))
prompt_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to generate email
button_frame = tk.Frame(frame, bg='#f0f0f0')
button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
generate_button = tk.Button(button_frame, text="Generate", command=lambda: generate_email(prompt_entry.get()), bg='#4CAF50', fg='white', width=15)
generate_button.pack(side=tk.LEFT, padx=5, pady=5)

# Response text area for displaying generated email
response_text_area = scrolledtext.ScrolledText(frame, height=20, width=70, bg='#ffffff', fg='#333333', font=("Helvetica", 12))
response_text_area.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Recipient email input
recipient_label = tk.Label(frame, text="Recipient Email:", bg='#f0f0f0', font=("Helvetica", 12), fg="#333333")
recipient_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
recipient_entry = tk.Entry(frame, width=50, font=("Helvetica", 12))
recipient_entry.grid(row=4, column=1, padx=5, pady=5)

# Subject input
subject_label = tk.Label(frame, text="Subject:", bg='#f0f0f0', font=("Helvetica", 12), fg="#333333")
subject_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
subject_entry = tk.Entry(frame, width=50, font=("Helvetica", 12))
subject_entry.grid(row=5, column=1, padx=5, pady=5)

# Button to send email
send_button = tk.Button(frame, text="Send Email", command=send_email_gui, bg='#4CAF50', fg='white', width=15)
send_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

# Start the Tkinter event loop
root.mainloop()


