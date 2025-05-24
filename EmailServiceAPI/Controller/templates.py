from .parser import plain_text_to_advanced_html
import urllib.parse


def encodedUPI(upi_url):
    return urllib.parse.quote(upi_url, safe='')


def simple(data):
    body_content = plain_text_to_advanced_html(data)
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <style>
        body {{
          margin: 0; padding: 0; background: #f4f6f8; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333;
        }}
        .container {{
          max-width: 640px;
          margin: 40px auto;
          background: #ffffff;
          border-radius: 8px;
          padding: 30px 40px;
          box-shadow: 0 0 20px rgba(0,0,0,0.08);
          box-sizing: border-box;
          word-wrap: break-word;
        }}
        h1, h2, h3 {{
          color: #222;
          margin-bottom: 12px;
        }}
        p {{
          line-height: 1.6;
          font-size: 16px;
          margin-bottom: 1.25em;
        }}
        ul, ol {{
          margin: 1em 0 1.25em 20px;
          padding: 0;
        }}
        li {{
          margin-bottom: 8px;
        }}
        a {{
          color: #1a73e8;
          text-decoration: none;
        }}
        a:hover {{
          text-decoration: underline;
        }}
        @media (max-width: 640px) {{
          .container {{
            margin: 20px;
            padding: 20px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="container" role="main" aria-label="Email content">
        {body_content}
      </div>
    </body>
    </html>"""


def Amazing(data, company_name: str | None):
    if company_name is None:
        company_name = "You've Got a New Message"
    body_content = plain_text_to_advanced_html(data)
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Notification Email</title>
      <style>
        body {{
          margin: 0;
          padding: 0;
          background-color: #eef2f6;
          font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
          color: #333;
        }}
        .wrapper {{
          width: 100%;
          padding: 40px 20px;
          display: flex;
          justify-content: center;
        }}
        .card {{
          background: #fff;
          max-width: 620px;
          width: 100%;
          border-radius: 12px;
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06);
          overflow: hidden;
        }}
        .header {{
          background-color: #0d9488;
          color: white;
          padding: 24px;
          text-align: left;
        }}
        .header h2 {{
          margin: 0;
          font-size: 22px;
          font-weight: 600;
        }}
        .content {{
          padding: 28px 32px;
          font-size: 16px;
          line-height: 1.65;
          background-color: #ffffff;
        }}
        .content p {{
          margin-bottom: 18px;
        }}
        .note {{
          font-size: 13px;
          color: #6b7280;
          margin-top: 28px;
          text-align: right;
        }}
        .footer {{
          background-color: #f1f5f9;
          text-align: center;
          font-size: 14px;
          padding: 20px;
          color: #6b7280;
          border-top: 1px solid #e5e7eb;
        }}
        .footer a {{
          color: #0f766e;
          text-decoration: none;
          font-weight: 500;
        }}
        .footer a:hover {{
          text-decoration: underline;
        }}
        @media (max-width: 640px) {{
          .card {{
            border-radius: 8px;
          }}
          .content {{
            padding: 24px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="wrapper">
        <div class="card" role="article" aria-label="User Message">
          <div class="header">
            <h2>{company_name}</h2>
          </div>
          <div class="content">
            {body_content}
            <div class="note">
              📬 This email was generated automatically. Please do not reply.
            </div>
          </div>
          <div class="footer">
            <p>
              © 2025 <a href="https://github.com/Sumit0ubey/" target="_blank">Sumit Dubey</a> — All rights reserved.
            </p>
          </div>
        </div>
      </div>
    </body>
    </html>"""


def cool(data, company_name: str | None):
    if company_name is None:
        company_name = "User Query"
    body_content = plain_text_to_advanced_html(data)
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Email Notification</title>
      <style>
        body {{
          margin: 0;
          padding: 0;
          background-color: #f4f7fc;
          font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
          color: #333;
        }}
        .email-container {{
          max-width: 600px;
          margin: 40px auto;
          background: #ffffff;
          border-radius: 16px;
          overflow: hidden;
          box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
          border: 1px solid #dee2e6;
        }}
        .email-header {{
          background: linear-gradient(90deg, #4f46e5, #3b82f6);
          color: #ffffff;
          padding: 24px 30px;
          text-align: center;
        }}
        .email-header h1 {{
          margin: 0;
          font-size: 24px;
          font-weight: 700;
          letter-spacing: 0.5px;
        }}
        .email-body {{
          padding: 32px;
          font-size: 16px;
          line-height: 1.75;
        }}
        .email-body p {{
          margin-bottom: 18px;
        }}
        .email-body strong {{
          color: #111827;
        }}
        .email-footer {{
          background-color: #f1f5f9;
          padding: 20px 30px;
          text-align: center;
          font-size: 14px;
          color: #6b7280;
          border-top: 1px solid #e5e7eb;
        }}
        .email-footer a {{
          color: #4b5563;
          text-decoration: none;
          margin: 0 6px;
        }}
        .email-footer a:hover {{
          text-decoration: underline;
        }}
        @media (max-width: 600px) {{
          .email-container {{
            margin: 20px;
          }}
          .email-body {{
            padding: 24px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="email-container" role="article" aria-label="Email Notification">
        <div class="email-header">
          <h1>{company_name}</h1>
        </div>
        <div class="email-body">
          {body_content}
          <p style="font-size: 13px; color: #9ca3af;">⚠️ This is an automated message. Please do not reply.</p>
        </div>
        <div class="email-footer">
          <p>
            Powered by <a href="https://github.com/Sumit0ubey/" target="_blank">Sumit Dubey</a> |
            <a href="#">Open Source</a>
          </p>
        </div>
      </div>
    </body>
    </html>"""


def custom(data, subject: str | None, company_name: str | None, company_link: str | None):
    project_info: str
    if company_name is None:
        company_name = "Sumit Dubey"
        project_info = "Open Source Project"
    else:
        project_info = "© All rights reserved"

    if company_link is None:
        company_link = "https://github.com/Sumit0ubey"

    if subject is None:
        subject = "You've Got a New Update"

    body_content = plain_text_to_advanced_html(data)
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Notification</title>
      <style>
        body {{
          margin: 0;
          padding: 0;
          background-color: #f3f4f6;
          font-family: 'Inter', sans-serif;
          color: #111827;
        }}
        .container {{
          max-width: 640px;
          margin: 50px auto;
          background-color: #ffffff;
          display: flex;
          border-radius: 12px;
          overflow: hidden;
          box-shadow: 0 12px 24px rgba(0,0,0,0.06);
        }}
        .sidebar {{
          background-color: #4b5563;
          width: 10px;
        }}
        .content {{
          padding: 40px;
          width: 100%;
        }}
        .title {{
          font-size: 20px;
          font-weight: 600;
          color: #1f2937;
          margin-bottom: 24px;
        }}
        .message {{
          font-size: 16px;
          line-height: 1.7;
          color: #374151;
          margin-bottom: 30px;
        }}
        .footer-note {{
          font-size: 13px;
          color: #9ca3af;
          text-align: right;
        }}
        .footer {{
          text-align: center;
          padding: 20px;
          font-size: 13px;
          color: #6b7280;
          border-top: 1px solid #e5e7eb;
          margin-top: 30px;
        }}
        .footer a {{
          color: #4b5563;
          text-decoration: none;
          margin: 0 6px;
        }}
        .footer a:hover {{
          text-decoration: underline;
        }}
        @media (max-width: 640px) {{
          .container {{
            flex-direction: row;
            flex-wrap: nowrap;
            margin: 10px;
            border-radius: 8px;
          }}
          .sidebar {{
            width: 6px;
            height: auto;
          }}
          .content {{
            padding: 20px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="container" role="article" aria-label="User Email">
        <div class="sidebar"></div>
        <div class="content">
          <div class="title">{subject}</div>
          <div class="message">
            {body_content}
          </div>
          <div class="footer-note">
            ⚠️ This is an automated email. No reply is needed.
          </div>
          <div class="footer">
            Sent via <a href={company_link} target="_blank">{company_name}</a> • 
            {project_info}
          </div>
        </div>
      </div>
    </body>
    </html>"""


def packagesPlan():
    upi_id = "sumit2003dubey@ibl"
    upi_redirect_url = "https://sumit0ubey.github.io/HelperWebPages/upi_redirect.html"
    card1 = f'{upi_redirect_url}?upi={encodedUPI(f"upi://pay?pa={upi_id}&pn=Email_Server_API&am=30&cu=INR&tn=Newbie_Pack")}'
    card2 = f'{upi_redirect_url}?upi={encodedUPI(f"upi://pay?pa={upi_id}&pn=Email_Server_API&am=300&cu=INR&tn=Veteran_Pack")}'
    card3 = f'{upi_redirect_url}?upi={encodedUPI(f"upi://pay?pa={upi_id}&pn=Email_Server_API&am=450&cu=INR&tn=Creator_Pack")}'
    card4 = f'{upi_redirect_url}?upi={encodedUPI(f"upi://pay?pa={upi_id}&pn=Email_Server_API&am=3423&cu=INR&tn=Owner_Pack")}'
    refund_policy_link = "#"
    return f"""
    <html lang="en"><head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Email Quota Packages</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f4f4f4;
          margin: 0;
          padding: 0;
        }}
        .email-container {{
          max-width: 600px;
          margin: auto;
          background-color: #ffffff;
          padding: 24px;
          border-radius: 10px;
          box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
        }}
        .email-container h2 {{
          text-align: center;
          color: #111827;
          font-size: 22px;
          margin-bottom: 30px;
        }}
        .card {{
          background-color: #ffffff;
          border-radius: 10px;
          box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
          padding: 20px;
          margin-bottom: 20px;
          text-align: center;
        }}
        .card h3 {{
          margin-top: 0;
          color: #1f2937;
          font-size: 18px;
        }}
        .card p {{
          color: #4b5563;
          font-size: 14px;
          margin: 10px 0;
        }}
        .price {{
          color: #e91e63;
          font-size: 20px;
          font-weight: bold;
          margin: 12px 0;
        }}
        .button {{
          background: linear-gradient(to right, #3b82f6, #2563eb);
          color: #ffffff;
          padding: 10px 24px;
          border-radius: 6px;
          text-decoration: none;
          font-weight: bold;
          font-size: 14px;
          display: inline-block;
          transition: background 0.3s ease;
        }}
        .button:hover {{
          background: linear-gradient(to right, #2563eb, #1d4ed8);
        }}
        .auto-note {{
          font-size: 12px;
          color: #9ca3af;
          text-align: center;
          margin: 20px 0;
        }}
        .footer {{
          text-align: center;
          font-size: 13px;
          color: #6b7280;
          border-top: 1px solid #e0e0e0;
          padding-top: 16px;
          margin-top: 30px;
        }}
        .footer a {{
          color: #3b82f6;
          text-decoration: none;
        }}
        .footer a:hover {{
          text-decoration: underline;
        }}
        @media only screen and (max-width: 620px) {{
          .email-container {{
            padding: 16px;
          }}
          .card {{
            padding: 16px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="email-container">
        <h2>Email Quota Packages</h2>
    
        <div class="card">
          <h3>Newbie Pack</h3>
          <p>Increases your email quota by 50 &amp; default by 3.</p>
          <div class="price">₹30.00</div>
          <a href="{card1}" class="button">Buy Now</a>
        </div>
    
        <div class="card">
          <h3>Veteran Pack</h3>
          <p>Increases your email quota by 699 &amp; default by 39.</p>
          <div class="price">₹299.99</div>
          <a href="{card2}" class="button">Buy Now</a>
        </div>
    
        <div class="card">
          <h3>Creator Pack</h3>
          <p>Increases default email service quota by 400.</p>
          <div class="price">₹449.99</div>
          <a href="{card3}" class="button">Buy Now</a>
        </div>
    
        <div class="card">
          <h3>Owner Pack</h3>
          <p>Increases your email quota by 99999.</p>
          <div class="price">₹3422.99</div>
          <a href="{card4}" class="button">Buy Now</a>
        </div>
    
        <div class="card">
          <p><strong>Note:</strong> After payment, please reply to this email with an attached payment receipt (screenshot) and transaction ID.</p>
        </div>
    
        <div class="auto-note">
          ⚠️ Please note: Any payment made is not refundable.<br>
          For more information, please review our Refund Policy.
        </div>
    
        <div class="footer">
          Sent by <a href="https://github.com/Sumit0ubey">Email Service API</a> • All rights reserved © 2025<br>
          <a href="{refund_policy_link}">Refund Policy</a>
        </div>
      </div>
    
    </body></html>
    """


def registrationEmail(iD: int, token: str):
    return f"""
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Registration Successful - Email Service API</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f4f4f4;
          margin: 0;
          padding: 0;
        }}
        .email-container {{
          max-width: 600px;
          margin: auto;
          background-color: #ffffff;
          padding: 24px;
          border-radius: 10px;
          box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
        }}
        .email-container h2 {{
          text-align: center;
          color: #111827;
          font-size: 22px;
          margin-bottom: 30px;
        }}
        .card {{
          background-color: #ffffff;
          border-radius: 10px;
          box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
          padding: 20px;
          margin-bottom: 20px;
          text-align: center;
        }}
        .card h3 {{
          margin-top: 0;
          color: #1f2937;
          font-size: 18px;
        }}
        .card p {{
          color: #4b5563;
          font-size: 14px;
          margin: 10px 0;
        }}
        .credentials {{
          color: #e91e63;
          font-size: 16px;
          font-weight: bold;
          margin: 12px 0;
          line-height: 1.6;
        }}
        .auto-note {{
          font-size: 12px;
          color: #9ca3af;
          text-align: center;
          margin: 20px 0;
        }}
        .footer {{
          text-align: center;
          font-size: 13px;
          color: #6b7280;
          border-top: 1px solid #e0e0e0;
          padding-top: 16px;
          margin-top: 30px;
        }}
        .footer a {{
          color: #3b82f6;
          text-decoration: none;
        }}
        .footer a:hover {{
          text-decoration: underline;
        }}
        @media only screen and (max-width: 620px) {{
          .email-container {{
            padding: 16px;
          }}
          .card {{
            padding: 16px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="email-container">
        <h2>Registration Successful</h2>
    
        <div class="card">
          <h3>Welcome to Email Service API</h3>
          <p>Thank you for registering with Email Service API. Below are your credentials:</p>
          <div class="credentials">
            ID: {iD} <br />
            Token: {token}
          </div>
        </div>
    
        <div class="card">
          <p><strong>Important:</strong> Do not share your ID or token and this mail with anyone.</p>
        </div>
    
        <div class="auto-note">
          ⚠️ This is an automated email. Please do not reply.
        </div>
    
        <div class="footer">
          Sent by <a href="https://github.com/Sumit0ubey">Email Service API</a> • All rights reserved © 2025<br />
        </div>
      </div>
    </body>
    </html>
    """


def tokenRevert(token: str):
    return f"""
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Registration Successful - Email Service API</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: #f4f4f4;
          margin: 0;
          padding: 0;
        }}
        .email-container {{
          max-width: 600px;
          margin: auto;
          background-color: #ffffff;
          padding: 24px;
          border-radius: 10px;
          box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
        }}
        .email-container h2 {{
          text-align: center;
          color: #111827;
          font-size: 22px;
          margin-bottom: 30px;
        }}
        .card {{
          background-color: #ffffff;
          border-radius: 10px;
          box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
          padding: 20px;
          margin-bottom: 20px;
          text-align: center;
        }}
        .card h3 {{
          margin-top: 0;
          color: #1f2937;
          font-size: 18px;
        }}
        .card p {{
          color: #4b5563;
          font-size: 14px;
          margin: 10px 0;
        }}
        .credentials {{
          color: #e91e63;
          font-size: 16px;
          font-weight: bold;
          margin: 12px 0;
          line-height: 1.6;
        }}
        .auto-note {{
          font-size: 12px;
          color: #9ca3af;
          text-align: center;
          margin: 20px 0;
        }}
        .footer {{
          text-align: center;
          font-size: 13px;
          color: #6b7280;
          border-top: 1px solid #e0e0e0;
          padding-top: 16px;
          margin-top: 30px;
        }}
        .footer a {{
          color: #3b82f6;
          text-decoration: none;
        }}
        .footer a:hover {{
          text-decoration: underline;
        }}
        @media only screen and (max-width: 620px) {{
          .email-container {{
            padding: 16px;
          }}
          .card {{
            padding: 16px;
          }}
        }}
      </style>
    </head>
    <body>
      <div class="email-container">
        <h2>Revert/Change Token </h2>

        <div class="card">
          <h3>Welcome to Email Service API</h3>
          <p>Thanks for sticking with us. Below is your new token:</p>
          <div class="credentials">
            Token: {token}
          </div>
        </div>

        <div class="card">
          <p><strong>Important:</strong> Do not share your token or this mail with anyone.</p>
        </div>

        <div class="auto-note">
          ⚠️ This is an automated email. Please do not reply.
        </div>

        <div class="footer">
          Sent by <a href="https://github.com/Sumit0ubey">Email Service API</a> • All rights reserved © 2025<br />
        </div>
      </div>
    </body>
    </html>
    """
