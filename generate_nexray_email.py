import base64

hero_path = r'd:\GitHub\BLENDER\hero_banner.jpg'
with open(hero_path, 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NEXRAY 3D // Client Asset Delivery</title>
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
                  <span style="display: inline-block; background-color: rgba(0, 56, 255, 0.08); color: #0038FF; font-size: 10px; font-weight: 800; letter-spacing: 1.5px; padding: 5px 12px; border-radius: 20px; border: 1px solid rgba(0, 56, 255, 0.25); text-transform: uppercase;">
                    OFFICIAL DISPATCH
                  </span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Hero Banner with Nexray Cobalt Blue & Neon Lime -->
        <tr>
          <td style="background: linear-gradient(135deg, #0038FF 0%, #001A99 100%); padding: 26px 28px; text-align: center;">
            <div style="display: inline-block; background-color: rgba(255, 255, 255, 0.15); color: #CCFF00; font-size: 10px; font-weight: 800; letter-spacing: 2px; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; margin-bottom: 10px; border: 1px solid rgba(204, 255, 0, 0.4);">
              &bull; PRODUCTION ASSET DELIVERY &bull;
            </div>
            <h1 style="margin: 0; font-family: 'Arial Black', Impact, sans-serif; font-size: 24px; font-weight: 900; color: #ffffff; letter-spacing: 0.5px; text-transform: uppercase;">
              LORD KODANDA RAMA
            </h1>
            <p style="margin: 6px 0 0 0; font-size: 13px; color: #e2e8f0; font-weight: 500;">
              6.00-Inch Custom Sculpt &bull; Slicer-Ready Binary STL
            </p>
          </td>
        </tr>

        <!-- Hero 3D Sculpture Showcase Image -->
        <tr>
          <td style="padding: 0; background-color: #0b1120; line-height: 0; text-align: center;">
            <img src="data:image/jpeg;base64,{b64_img}" alt="Lord Kodanda Rama 3D Sculpt" width="100%" style="display: block; max-width: 620px; height: auto; border: 0;" />
          </td>
        </tr>

        <!-- Order / Invoice Status Bar -->
        <tr>
          <td style="padding: 16px 28px; background-color: #f8fafc; border-bottom: 1px solid #e2e8f0;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
              <tr>
                <td align="left" style="font-size: 13px; color: #475569;">
                  Status: <strong style="color: #16a34a;">&bull; Quality Verified &amp; Ready</strong>
                </td>
                <td align="right" style="font-size: 13px; color: #475569;">
                  Agreed Rate: <strong style="color: #0f172a; font-size: 15px;">&#8377;1,500</strong>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Main Body & Action Button -->
        <tr>
          <td style="padding: 28px 28px 32px 28px; background-color: #ffffff;">
            
            <p style="font-size: 14px; color: #334155; line-height: 1.7; margin: 0 0 22px 0;">
              Hi bro, your commissioned 3D production model for <strong>Lord Kodanda Rama</strong> has passed our studio verification pipeline. It is pre-calibrated to exactly <strong>6.00 inches (152.4 mm)</strong> with a 100% watertight, single-shell manifold topology.
            </p>

            <!-- Primary Nexray Cobalt Blue Download Button -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin: 26px 0;">
              <tr>
                <td align="center">
                  <a href="PASTE_YOUR_GOOGLE_DRIVE_OR_DROPBOX_LINK_HERE" target="_blank" style="display: inline-block; background: #0038FF; color: #ffffff; font-size: 15px; font-weight: 800; text-decoration: none; padding: 16px 38px; border-radius: 9999px; box-shadow: 0 8px 24px rgba(0, 56, 255, 0.35); letter-spacing: 0.5px; text-transform: uppercase;">
                    &darr; ACCESS PRODUCTION FILES (.ZIP &bull; 42 MB)
                  </a>
                </td>
              </tr>
              <tr>
                <td align="center" style="padding-top: 10px;">
                  <span style="font-size: 11px; color: #64748b; letter-spacing: 0.5px;">
                    Verified archive containing full-resolution binary STL &bull; Zero slicer errors
                  </span>
                </td>
              </tr>
            </table>

            <!-- 4-Box Technical Blueprint Grid -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 24px; margin-bottom: 24px;">
              <tr>
                <!-- Box 1 -->
                <td width="48%" valign="top" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 800; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">PHYSICAL HEIGHT</div>
                  <div style="font-size: 18px; font-weight: 800; color: #0f172a; margin-top: 3px;">152.40 mm</div>
                  <div style="font-size: 11px; color: #64748b;">Calibrated 6.00" Target Scale</div>
                </td>
                <td width="4%"></td>
                <!-- Box 2 -->
                <td width="48%" valign="top" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 800; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">GEOMETRY DETAIL</div>
                  <div style="font-size: 18px; font-weight: 800; color: #0038FF; margin-top: 3px;">2.20M Triangles</div>
                  <div style="font-size: 11px; color: #64748b;">Ultra-High Surface Detail</div>
                </td>
              </tr>
              <tr><td height="12" colspan="3"></td></tr>
              <tr>
                <!-- Box 3 -->
                <td width="48%" valign="top" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 800; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">FIRST LAYER CONTACT</div>
                  <div style="font-size: 18px; font-weight: 800; color: #0f172a; margin-top: 3px;">Z = 0.00 mm</div>
                  <div style="font-size: 11px; color: #64748b;">Zero-Wobble Planar Base</div>
                </td>
                <td width="4%"></td>
                <!-- Box 4 -->
                <td width="48%" valign="top" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 800; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">TOPOLOGY HEALTH</div>
                  <div style="font-size: 18px; font-weight: 800; color: #16a34a; margin-top: 3px;">100% Manifold</div>
                  <div style="font-size: 11px; color: #64748b;">0 Non-Manifold / 0 Holes</div>
                </td>
              </tr>
            </table>

            <!-- Recommended Manufacturing Guidelines -->
            <div style="margin-top: 26px;">
              <div style="font-size: 11px; font-weight: 800; color: #0038FF; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 12px;">
                &bull; RECOMMENDED MANUFACTURING PARAMETERS
              </div>

              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                <tr>
                  <!-- FDM Card -->
                  <td width="48%" valign="top" style="background-color: #f8fafc; border-left: 3px solid #0038FF; border-radius: 8px; padding: 14px 16px;">
                    <div style="font-size: 12px; font-weight: 800; color: #0038FF; text-transform: uppercase; letter-spacing: 0.5px;">FDM (Filament)</div>
                    <ul style="margin: 8px 0 0 0; padding-left: 16px; font-size: 12px; color: #475569; line-height: 1.7;">
                      <li><strong>Supports:</strong> Tree / Organic enabled</li>
                      <li><strong>Layer Height:</strong> 0.12 mm &ndash; 0.16 mm</li>
                      <li><strong>Infill:</strong> 15% &ndash; 20% (Gyroid)</li>
                      <li><strong>Raft:</strong> None required</li>
                    </ul>
                  </td>
                  <td width="4%"></td>
                  <!-- Resin Card -->
                  <td width="48%" valign="top" style="background-color: #f8fafc; border-left: 3px solid #7c3aed; border-radius: 8px; padding: 14px 16px;">
                    <div style="font-size: 12px; font-weight: 800; color: #7c3aed; text-transform: uppercase; letter-spacing: 0.5px;">Resin (SLA / DLP)</div>
                    <ul style="margin: 8px 0 0 0; padding-left: 16px; font-size: 12px; color: #475569; line-height: 1.7;">
                      <li><strong>Orientation:</strong> 35&deg; &ndash; 45&deg; tilt backward</li>
                      <li><strong>Supports:</strong> Light/Medium touchpoints</li>
                      <li><strong>Layer Height:</strong> 0.05 mm (High Detail)</li>
                      <li><strong>Hollowing:</strong> Optional (2 mm shell)</li>
                    </ul>
                  </td>
                </tr>
              </table>
            </div>

            <!-- Sign-off & Studio Info -->
            <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #e2e8f0;">
              <p style="margin: 0; font-size: 13px; color: #475569; line-height: 1.7;">
                Ready for immediate import into Bambu Studio, OrcaSlicer, PrusaSlicer, or Chitubox. Reach out if you have any questions about slicing or orientation!
              </p>
              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 18px;">
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

        <!-- Brand Footer -->
        <tr>
          <td style="background-color: #f8fafc; padding: 20px 28px; text-align: center; border-top: 1px solid #e2e8f0;">
            <p style="margin: 0; font-size: 11px; font-weight: 700; color: #64748b; letter-spacing: 1px; text-transform: uppercase;">
              NEXRAY 3D DIGITAL ATELIER &bull; ALL RIGHTS RESERVED
            </p>
            <p style="margin: 4px 0 0 0; font-size: 10px; color: #94a3b8;">
              A division of <a href="https://nexray.in" style="color: #0038FF; text-decoration: none; font-weight: 600;">nexray.in</a> &bull; Verified 100% Watertight Deliverable
            </p>
          </td>
        </tr>

      </table>

    </td>
  </tr>
</table>

</body>
</html>'''

workspace_path = r'd:\GitHub\BLENDER\NexRay_Brand_Delivery_Email.html'
desktop_path = r'C:\Users\divya\Desktop\NexRay_Brand_Delivery_Email.html'

with open(workspace_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(desktop_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated NexRay Brand Email matching nexray.in created successfully!")
