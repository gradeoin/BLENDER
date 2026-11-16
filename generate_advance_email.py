import base64

hero_path = r'd:\GitHub\BLENDER\hero_banner.jpg'
with open(hero_path, 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NEXRAY 3D // Order Confirmation &amp; Advance Receipt</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f1f5f9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #0f172a; line-height: 1.6;">

<!-- Outer Email Wrapper -->
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #f1f5f9; padding: 36px 12px;">
  <tr>
    <td align="center">
      
      <!-- Main Brand Card -->
      <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="max-width: 620px; background-color: #ffffff; border-radius: 16px; overflow: hidden; border: 1px solid rgba(0, 56, 255, 0.12); box-shadow: 0 12px 36px rgba(0, 56, 255, 0.10);">
        
        <!-- Top Navigation Bar matching nexray.in -->
        <tr>
          <td style="background-color: #ffffff; padding: 18px 28px; border-bottom: 2px solid #0038FF;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
              <tr>
                <td align="left">
                  <table role="presentation" cellspacing="0" cellpadding="0" border="0">
                    <tr>
                      <td valign="middle">
                        <img src="https://res.cloudinary.com/djy0vsvfg/image/upload/v1774822889/logo_highres_hdmcey.png" alt="Nexray Logo" width="34" height="34" style="display: block; border-radius: 6px; box-shadow: 0 4px 10px rgba(0, 56, 255, 0.25);" />
                      </td>
                      <td valign="middle" style="padding-left: 10px;">
                        <span style="font-family: 'Arial Black', Impact, sans-serif; font-size: 20px; font-weight: 900; letter-spacing: 1px; color: #0f172a; text-transform: uppercase;">
                          NEX<span style="color: #0038FF;">RAY</span>
                        </span>
                        <span style="font-size: 11px; font-weight: 800; color: #64748b; letter-spacing: 1.5px; margin-left: 4px;">// 3D</span>
                      </td>
                    </tr>
                  </table>
                </td>
                <td align="right" valign="middle">
                  <span style="display: inline-block; background-color: rgba(22, 163, 74, 0.1); color: #16a34a; font-size: 10px; font-weight: 800; letter-spacing: 1.5px; padding: 5px 12px; border-radius: 20px; border: 1px solid rgba(22, 163, 74, 0.25); text-transform: uppercase;">
                    ADVANCE RECEIVED
                  </span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Hero Header -->
        <tr>
          <td style="background: linear-gradient(135deg, #0038FF 0%, #001A99 100%); padding: 26px 28px; text-align: center;">
            <div style="display: inline-block; background-color: rgba(255, 255, 255, 0.15); color: #CCFF00; font-size: 10px; font-weight: 800; letter-spacing: 2px; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; margin-bottom: 10px; border: 1px solid rgba(204, 255, 0, 0.4);">
              &bull; OFFICIAL COMMISSION RECEIPT &bull;
            </div>
            <h1 style="margin: 0; font-family: 'Arial Black', Impact, sans-serif; font-size: 24px; font-weight: 900; color: #ffffff; letter-spacing: 0.5px; text-transform: uppercase;">
              ORDER CONFIRMATION
            </h1>
            <p style="margin: 6px 0 0 0; font-size: 13px; color: #e2e8f0; font-weight: 500;">
              Lord Kodanda Rama &bull; 6.00-Inch Custom Production Master
            </p>
          </td>
        </tr>

        <!-- Hero Preview Image -->
        <tr>
          <td style="padding: 0; background-color: #0b1120; line-height: 0; text-align: center;">
            <img src="data:image/jpeg;base64,{b64_img}" alt="Lord Kodanda Rama 3D Sculpt" width="100%" style="display: block; max-width: 620px; height: auto; border: 0;" />
          </td>
        </tr>

        <!-- Body & Financial Statement -->
        <tr>
          <td style="padding: 28px 28px 32px 28px; background-color: #ffffff;">
            
            <p style="font-size: 14px; color: #334155; line-height: 1.7; margin: 0 0 20px 0;">
              Hi bro, thanks for sending over the advance! This email confirms your commission order for the <strong>Lord Kodanda Rama 6-Inch 3D Print Master Sculpt</strong>.
            </p>

            <!-- Invoice Summary Box -->
            <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px 20px; margin-bottom: 24px;">
              <div style="font-size: 11px; font-weight: 800; color: #0038FF; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 12px;">
                FINANCIAL STATEMENT
              </div>
              <table role="presentation" width="100%" cellspacing="0" cellpadding="6" border="0" style="font-size: 13px; color: #334155;">
                <tr>
                  <td>Total Agreed Commission:</td>
                  <td align="right"><strong>&#8377;1,500</strong></td>
                </tr>
                <tr>
                  <td>Advance Payment Received:</td>
                  <td align="right" style="color: #16a34a;"><strong>&minus; &#8377;750</strong></td>
                </tr>
                <tr style="border-top: 1px solid #cbd5e1;">
                  <td style="padding-top: 10px;"><strong>Remaining Balance on Delivery:</strong></td>
                  <td align="right" style="padding-top: 10px; font-size: 15px; color: #0f172a;"><strong>&#8377;750</strong></td>
                </tr>
              </table>
            </div>

            <!-- Milestone Progress -->
            <div style="background-color: rgba(0, 56, 255, 0.04); border-left: 3px solid #0038FF; border-radius: 6px; padding: 14px 18px; margin-bottom: 24px; font-size: 13px; color: #334155; line-height: 1.7;">
              <strong>Current Milestone:</strong> 3D geometry is 100% complete and watertight verified. The final binary STL package (42 MB) will be unlocked and dispatched immediately upon balance clearance.
            </div>

            <!-- Sign-off & Studio Info -->
            <div style="margin-top: 28px; padding-top: 20px; border-top: 1px solid #e2e8f0;">
              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                <tr>
                  <td align="left">
                    <div style="font-size: 15px; font-weight: 800; color: #0f172a;">Divyansh Aggarwal</div>
                    <div style="font-size: 12px; color: #0038FF; font-weight: 700;">NEXRAY 3D &bull; Digital Manufacturing</div>
                    <div style="font-size: 11px; color: #64748b; margin-top: 2px;">info@nexray.in &bull; <a href="https://studio.nexray.in" style="color: #0038FF; text-decoration: none; font-weight: 600;">studio.nexray.in</a></div>
                  </td>
                </tr>
              </table>
            </div>

          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td style="background-color: #f8fafc; padding: 20px 28px; text-align: center; border-top: 1px solid #e2e8f0;">
            <p style="margin: 0; font-size: 11px; font-weight: 700; color: #64748b; letter-spacing: 1px; text-transform: uppercase;">
              NEXRAY 3D DIGITAL ATELIER &bull; ALL RIGHTS RESERVED
            </p>
            <p style="margin: 4px 0 0 0; font-size: 10px; color: #94a3b8;">
              A division of <a href="https://nexray.in" style="color: #0038FF; text-decoration: none; font-weight: 600;">nexray.in</a>
            </p>
          </td>
        </tr>

      </table>

    </td>
  </tr>
</table>

</body>
</html>'''

workspace_path = r'd:\GitHub\BLENDER\NexRay_Advance_Invoice_Email.html'
desktop_path = r'C:\Users\divya\Desktop\NexRay_Advance_Invoice_Email.html'

with open(workspace_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(desktop_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("NexRay Advance Invoice Email created successfully!")
