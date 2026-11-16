import base64
import os

hero_path = r'd:\GitHub\BLENDER\hero_banner.jpg'
with open(hero_path, 'rb') as f:
    b64_img = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lord Rama 6-Inch 3D Printable STL - Master Delivery</title>
</head>
<body style="margin: 0; padding: 0; background-color: #090d16; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #e2e8f0; line-height: 1.6;">

<!-- Outer Luxury Wrapper -->
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #090d16; padding: 40px 15px;">
  <tr>
    <td align="center">
      
      <!-- Main Container Card -->
      <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="max-width: 640px; background-color: #111827; border-radius: 16px; overflow: hidden; border: 1px solid rgba(212, 175, 55, 0.35); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);">
        
        <!-- Top Studio Bar -->
        <tr>
          <td style="background-color: #0c101c; padding: 18px 32px; border-bottom: 1px solid rgba(212, 175, 55, 0.2);">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
              <tr>
                <td align="left">
                  <span style="font-size: 11px; font-weight: 800; letter-spacing: 2.5px; color: #d4af37; text-transform: uppercase;">
                    DIVYANSH AGGARWAL &#8226; 3D ATELIER
                  </span>
                </td>
                <td align="right">
                  <span style="display: inline-block; background-color: rgba(212, 175, 55, 0.15); color: #f6e05e; font-size: 10px; font-weight: 700; letter-spacing: 1.5px; padding: 4px 10px; border-radius: 20px; border: 1px solid rgba(212, 175, 55, 0.4); text-transform: uppercase;">
                    MASTER RELEASE
                  </span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Hero 3D Sculpture Image (Embedded directly in Base64) -->
        <tr>
          <td style="padding: 0; background-color: #111827; line-height: 0; text-align: center;">
            <img src="data:image/jpeg;base64,{b64_img}" alt="Lord Kodanda Rama 3D Sculpt" width="100%" style="display: block; max-width: 640px; height: auto; border: 0;" />
          </td>
        </tr>

        <!-- Title Section -->
        <tr>
          <td style="padding: 24px 36px 8px 36px; text-align: center; background-color: #111827;">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 3px; color: #a0aec0; text-transform: uppercase; margin-bottom: 6px;">
              PRECISION COLLECTIBLE EDITION
            </div>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #ffffff; letter-spacing: 0.5px; text-transform: uppercase;">
              LORD KODANDA RAMA
            </h1>
            <p style="margin: 6px 0 0 0; font-size: 14px; color: #d4af37; font-weight: 600; letter-spacing: 1px;">
              6.00-INCH PRODUCTION-READY 3D STL
            </p>
          </td>
        </tr>

        <!-- Order / Investment Confirmation Strip -->
        <tr>
          <td style="padding: 14px 36px; background-color: #111827;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="12" border="0" style="background-color: #1a202c; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px;">
              <tr>
                <td align="left" style="font-size: 13px; color: #a0aec0;">
                  Order Status: <strong style="color: #48bb78;">&#8226; Verified &amp; Ready</strong>
                </td>
                <td align="right" style="font-size: 13px; color: #a0aec0;">
                  Agreed Price: <strong style="color: #ffffff; font-size: 15px;">&#8377;1,500</strong>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Main Body & Action Button -->
        <tr>
          <td style="padding: 10px 36px 32px 36px; background-color: #111827;">
            
            <p style="font-size: 14px; color: #cbd5e0; line-height: 1.7; margin: 0 0 24px 0;">
              Hi bro, your master 3D model for <strong>Lord Kodanda Rama</strong> is 100% complete and verified. Every detail has been sculpted for high-precision physical output—including the sacred Kodanda bow, 4-arrow quiver bundle, authentic Varada Mudra hand posture, and ornate Mukut crown.
            </p>

            <!-- Prominent Gold Call to Action Button -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin: 28px 0;">
              <tr>
                <td align="center">
                  <a href="PASTE_YOUR_GOOGLE_DRIVE_OR_DROPBOX_LINK_HERE" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #d4af37 0%, #aa771c 50%, #f7e08b 100%); color: #000000; font-size: 15px; font-weight: 800; text-decoration: none; padding: 16px 38px; border-radius: 8px; box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4); letter-spacing: 0.5px; text-transform: uppercase;">
                    &#8595; DOWNLOAD 3D STL MASTER FILE (42 MB)
                  </a>
                </td>
              </tr>
              <tr>
                <td align="center" style="padding-top: 10px;">
                  <span style="font-size: 11px; color: #718096; letter-spacing: 0.5px;">
                    Delivered as verified zip archive &#8226; 100% Manifold Watertight Shell
                  </span>
                </td>
              </tr>
            </table>

            <!-- 4-Box Technical Blueprint Grid -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 24px; margin-bottom: 24px;">
              <tr>
                <!-- Box 1 -->
                <td width="48%" valign="top" style="background-color: #1a202c; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #a0aec0; letter-spacing: 1.5px; text-transform: uppercase;">TOTAL HEIGHT</div>
                  <div style="font-size: 18px; font-weight: 800; color: #ffffff; margin-top: 4px;">152.40 mm</div>
                  <div style="font-size: 11px; color: #718096;">Exact 6.00 Inches Calibrated</div>
                </td>
                <td width="4%"></td>
                <!-- Box 2 -->
                <td width="48%" valign="top" style="background-color: #1a202c; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #a0aec0; letter-spacing: 1.5px; text-transform: uppercase;">POLYGON DETAIL</div>
                  <div style="font-size: 18px; font-weight: 800; color: #d4af37; margin-top: 4px;">2.20 Million</div>
                  <div style="font-size: 11px; color: #718096;">Ultra-High Density Triangles</div>
                </td>
              </tr>
              <tr><td height="12" colspan="3"></td></tr>
              <tr>
                <!-- Box 3 -->
                <td width="48%" valign="top" style="background-color: #1a202c; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #a0aec0; letter-spacing: 1.5px; text-transform: uppercase;">BED ADHESION</div>
                  <div style="font-size: 18px; font-weight: 800; color: #ffffff; margin-top: 4px;">Z = 0.00 mm</div>
                  <div style="font-size: 11px; color: #718096;">Mathematically Flat Contact</div>
                </td>
                <td width="4%"></td>
                <!-- Box 4 -->
                <td width="48%" valign="top" style="background-color: #1a202c; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #a0aec0; letter-spacing: 1.5px; text-transform: uppercase;">TOPOLOGY</div>
                  <div style="font-size: 18px; font-weight: 800; color: #48bb78; margin-top: 4px;">100% Watertight</div>
                  <div style="font-size: 11px; color: #718096;">0 Non-Manifold / 0 Holes</div>
                </td>
              </tr>
            </table>

            <!-- Recommended Production Slicing Cards -->
            <div style="margin-top: 26px;">
              <div style="font-size: 11px; font-weight: 800; color: #d4af37; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px;">
                &#8226; PRODUCTION SLICING SPECIFICATIONS
              </div>

              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                <tr>
                  <!-- FDM Card -->
                  <td width="48%" valign="top" style="background: linear-gradient(180deg, #161e2e 0%, #111827 100%); border: 1px solid rgba(99, 179, 237, 0.25); border-radius: 8px; padding: 16px;">
                    <div style="font-size: 12px; font-weight: 700; color: #63b3ed; text-transform: uppercase; letter-spacing: 1px;">FDM (Filament)</div>
                    <ul style="margin: 8px 0 0 0; padding-left: 16px; font-size: 12px; color: #a0aec0; line-height: 1.7;">
                      <li><strong>Supports:</strong> Tree / Organic enabled</li>
                      <li><strong>Layer Height:</strong> 0.12 mm &#8211; 0.16 mm</li>
                      <li><strong>Infill:</strong> 15% &#8211; 20% (Gyroid)</li>
                      <li><strong>Seams:</strong> Aligned / Back</li>
                    </ul>
                  </td>
                  <td width="4%"></td>
                  <!-- Resin Card -->
                  <td width="48%" valign="top" style="background: linear-gradient(180deg, #1c182c 0%, #111827 100%); border: 1px solid rgba(183, 148, 244, 0.25); border-radius: 8px; padding: 16px;">
                    <div style="font-size: 12px; font-weight: 700; color: #b794f4; text-transform: uppercase; letter-spacing: 1px;">Resin (SLA / DLP)</div>
                    <ul style="margin: 8px 0 0 0; padding-left: 16px; font-size: 12px; color: #a0aec0; line-height: 1.7;">
                      <li><strong>Orientation:</strong> 35&deg; &#8211; 45&deg; tilt backward</li>
                      <li><strong>Supports:</strong> Light/Medium touchpoints</li>
                      <li><strong>Layer Height:</strong> 0.05 mm (High Detail)</li>
                      <li><strong>Hollowing:</strong> Optional (2 mm shell)</li>
                    </ul>
                  </td>
                </tr>
              </table>
            </div>

            <!-- Sign-off -->
            <div style="margin-top: 32px; padding-top: 20px; border-top: 1px solid rgba(255, 255, 255, 0.08);">
              <p style="margin: 0; font-size: 14px; color: #cbd5e0;">
                Drop this file directly into Bambu Studio, OrcaSlicer, PrusaSlicer, or Chitubox&#8212;it will load at exact 1:1 scale with zero manifold repair prompts. Reach out anytime if you want advice on slicer orientation!
              </p>
              <p style="margin: 18px 0 0 0; font-size: 14px; color: #718096;">
                Best regards,<br>
                <strong style="color: #ffffff;">Divyansh Aggarwal</strong><br>
                <span style="font-size: 12px; color: #d4af37;">Digital Sculptor &amp; 3D Production</span>
              </p>
            </div>

          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td style="background-color: #0c101c; padding: 22px 36px; text-align: center; border-top: 1px solid rgba(212, 175, 55, 0.2);">
            <p style="margin: 0; font-size: 11px; color: #718096; letter-spacing: 0.5px;">
              Lord Kodanda Rama &#8226; Production Master Edition &#8226; Personal &amp; Commercial Print License
            </p>
            <p style="margin: 6px 0 0 0; font-size: 10px; color: #4a5568;">
              Delivered by Divyansh Aggarwal 3D Studio &#8226; Verified 100% Watertight
            </p>
          </td>
        </tr>

      </table>

    </td>
  </tr>
</table>

</body>
</html>'''

workspace_path = r'd:\GitHub\BLENDER\Rama_Brand_Delivery_Email.html'
desktop_path = r'C:\Users\divya\Desktop\Rama_Brand_Delivery_Email.html'

with open(workspace_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(desktop_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Brand HTML email created successfully at:")
print(f" - {workspace_path}")
print(f" - {desktop_path}")
