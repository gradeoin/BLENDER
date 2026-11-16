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
<body style="margin: 0; padding: 0; background-color: #07090e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #e2e8f0; line-height: 1.6;">

<!-- Outer Dark Wrapper -->
<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="background-color: #07090e; background-image: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.08) 0%, transparent 60%); padding: 40px 15px;">
  <tr>
    <td align="center">
      
      <!-- Main Brand Card -->
      <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="max-width: 640px; background-color: #0f172a; border-radius: 16px; overflow: hidden; border: 1px solid rgba(56, 189, 248, 0.25); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.85);">
        
        <!-- NEXRAY Brand Top Header -->
        <tr>
          <td style="background-color: #0b1120; padding: 22px 36px; border-bottom: 1px solid rgba(56, 189, 248, 0.15);">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
              <tr>
                <td align="left">
                  <div style="font-size: 20px; font-weight: 900; letter-spacing: 3.5px; color: #ffffff; text-transform: uppercase;">
                    NEX<span style="color: #38bdf8;">RAY</span> <span style="font-size: 11px; font-weight: 700; color: #94a3b8; letter-spacing: 2px;">// 3D</span>
                  </div>
                  <div style="font-size: 9px; font-weight: 700; letter-spacing: 2px; color: #64748b; text-transform: uppercase; margin-top: 3px;">
                    DIGITAL SCULPT &amp; ADDITIVE MANUFACTURING
                  </div>
                </td>
                <td align="right">
                  <span style="display: inline-block; background-color: rgba(56, 189, 248, 0.12); color: #38bdf8; font-size: 10px; font-weight: 700; letter-spacing: 1.5px; padding: 5px 12px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.35); text-transform: uppercase;">
                    OFFICIAL DISPATCH
                  </span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Project Hero Showcase Frame -->
        <tr>
          <td style="padding: 0; background-color: #0f172a; line-height: 0; text-align: center;">
            <img src="data:image/jpeg;base64,{b64_img}" alt="Project 3D Render" width="100%" style="display: block; max-width: 640px; height: auto; border: 0;" />
          </td>
        </tr>

        <!-- Project Title Header -->
        <tr>
          <td style="padding: 28px 36px 10px 36px; text-align: center; background-color: #0f172a;">
            <div style="font-size: 11px; font-weight: 700; letter-spacing: 2.5px; color: #38bdf8; text-transform: uppercase; margin-bottom: 6px;">
              PRODUCTION ASSET DELIVERY
            </div>
            <h1 style="margin: 0; font-size: 26px; font-weight: 800; color: #ffffff; letter-spacing: 0.5px; text-transform: uppercase;">
              LORD KODANDA RAMA
            </h1>
            <p style="margin: 6px 0 0 0; font-size: 14px; color: #94a3b8; font-weight: 500; letter-spacing: 0.5px;">
              6.00-Inch Custom Sculpt &bull; Slicer-Ready Binary STL
            </p>
          </td>
        </tr>

        <!-- Invoice / Order Badge -->
        <tr>
          <td style="padding: 14px 36px; background-color: #0f172a;">
            <table role="presentation" width="100%" cellspacing="0" cellpadding="12" border="0" style="background-color: #1e293b; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px;">
              <tr>
                <td align="left" style="font-size: 13px; color: #94a3b8;">
                  Status: <strong style="color: #34d399;">&bull; Quality Verified &amp; Ready</strong>
                </td>
                <td align="right" style="font-size: 13px; color: #94a3b8;">
                  Project Invoice: <strong style="color: #ffffff; font-size: 15px;">&#8377;1,500</strong>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Delivery Body & Download Action -->
        <tr>
          <td style="padding: 10px 36px 32px 36px; background-color: #0f172a;">
            
            <p style="font-size: 14px; color: #cbd5e1; line-height: 1.7; margin: 0 0 24px 0;">
              Your commissioned 3D production model has passed our studio verification pipeline. The geometry has been inspected for 100% manifold watertightness, true bed-adhesion planar contact, and calibrated to exact physical build dimensions.
            </p>

            <!-- Primary Cyan Download Button -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin: 28px 0;">
              <tr>
                <td align="center">
                  <a href="PASTE_YOUR_GOOGLE_DRIVE_OR_DROPBOX_LINK_HERE" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%); color: #ffffff; font-size: 15px; font-weight: 800; text-decoration: none; padding: 16px 42px; border-radius: 8px; box-shadow: 0 8px 24px rgba(56, 189, 248, 0.35); letter-spacing: 0.5px; text-transform: uppercase;">
                    &darr; ACCESS PRODUCTION FILES (.ZIP &bull; 42 MB)
                  </a>
                </td>
              </tr>
              <tr>
                <td align="center" style="padding-top: 10px;">
                  <span style="font-size: 11px; color: #64748b; letter-spacing: 0.5px;">
                    Verified archive containing full-resolution binary STL &bull; Single-shell solid
                  </span>
                </td>
              </tr>
            </table>

            <!-- 4-Box Technical Blueprint Grid -->
            <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 24px; margin-bottom: 24px;">
              <tr>
                <!-- Box 1 -->
                <td width="48%" valign="top" style="background-color: #1e293b; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">PHYSICAL HEIGHT</div>
                  <div style="font-size: 18px; font-weight: 800; color: #ffffff; margin-top: 4px;">152.40 mm</div>
                  <div style="font-size: 11px; color: #94a3b8;">Calibrated 6.00" Target Scale</div>
                </td>
                <td width="4%"></td>
                <!-- Box 2 -->
                <td width="48%" valign="top" style="background-color: #1e293b; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">GEOMETRY DENSITY</div>
                  <div style="font-size: 18px; font-weight: 800; color: #38bdf8; margin-top: 4px;">2.20M Triangles</div>
                  <div style="font-size: 11px; color: #94a3b8;">High-Fidelity Surface Detail</div>
                </td>
              </tr>
              <tr><td height="12" colspan="3"></td></tr>
              <tr>
                <!-- Box 3 -->
                <td width="48%" valign="top" style="background-color: #1e293b; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">FIRST LAYER CONTACT</div>
                  <div style="font-size: 18px; font-weight: 800; color: #ffffff; margin-top: 4px;">Z = 0.00 mm</div>
                  <div style="font-size: 11px; color: #94a3b8;">Zero-Wobble Planar Base</div>
                </td>
                <td width="4%"></td>
                <!-- Box 4 -->
                <td width="48%" valign="top" style="background-color: #1e293b; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 16px;">
                  <div style="font-size: 10px; font-weight: 700; color: #64748b; letter-spacing: 1.5px; text-transform: uppercase;">TOPOLOGY HEALTH</div>
                  <div style="font-size: 18px; font-weight: 800; color: #34d399; margin-top: 4px;">100% Manifold</div>
                  <div style="font-size: 11px; color: #94a3b8;">0 Non-Manifold / 0 Holes</div>
                </td>
              </tr>
            </table>

            <!-- Slicing Profiles Section -->
            <div style="margin-top: 26px;">
              <div style="font-size: 11px; font-weight: 800; color: #38bdf8; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px;">
                &bull; RECOMMENDED MANUFACTURING PARAMETERS
              </div>

              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
                <tr>
                  <!-- FDM Card -->
                  <td width="48%" valign="top" style="background: linear-gradient(180deg, #132338 0%, #0f172a 100%); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 16px;">
                    <div style="font-size: 12px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 1px;">FDM (Filament)</div>
                    <ul style="margin: 8px 0 0 0; padding-left: 16px; font-size: 12px; color: #94a3b8; line-height: 1.7;">
                      <li><strong>Supports:</strong> Tree / Organic enabled</li>
                      <li><strong>Layer Height:</strong> 0.12 mm &ndash; 0.16 mm</li>
                      <li><strong>Infill:</strong> 15% &ndash; 20% (Gyroid)</li>
                      <li><strong>Raft:</strong> None required (True flat base)</li>
                    </ul>
                  </td>
                  <td width="4%"></td>
                  <!-- Resin Card -->
                  <td width="48%" valign="top" style="background: linear-gradient(180deg, #1e1b38 0%, #0f172a 100%); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 8px; padding: 16px;">
                    <div style="font-size: 12px; font-weight: 700; color: #c084fc; text-transform: uppercase; letter-spacing: 1px;">Resin (SLA / DLP)</div>
                    <ul style="margin: 8px 0 0 0; padding-left: 16px; font-size: 12px; color: #94a3b8; line-height: 1.7;">
                      <li><strong>Orientation:</strong> 35&deg; &ndash; 45&deg; tilt backward</li>
                      <li><strong>Supports:</strong> Light/Medium touchpoints</li>
                      <li><strong>Layer Height:</strong> 0.05 mm (High Detail)</li>
                      <li><strong>Hollowing:</strong> Optional (2 mm shell)</li>
                    </ul>
                  </td>
                </tr>
              </table>
            </div>

            <!-- Studio Support & Sign-off -->
            <div style="margin-top: 32px; padding-top: 20px; border-top: 1px solid rgba(255, 255, 255, 0.08);">
              <p style="margin: 0; font-size: 13px; color: #cbd5e1; line-height: 1.7;">
                Ready for immediate import into Bambu Studio, OrcaSlicer, PrusaSlicer, or Chitubox. If you require custom scaling, alternative file formats (.STEP, .OBJ, .3MF), or slicing orientation advice, contact the studio directly.
              </p>
              <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin-top: 20px;">
                <tr>
                  <td align="left">
                    <div style="font-size: 15px; font-weight: 800; color: #ffffff;">Divyansh Aggarwal</div>
                    <div style="font-size: 12px; color: #38bdf8; font-weight: 600;">Lead 3D Artist &bull; NEXRAY 3D</div>
                    <div style="font-size: 11px; color: #64748b; margin-top: 2px;">contact@nexray.in</div>
                  </td>
                </tr>
              </table>
            </div>

          </td>
        </tr>

        <!-- Brand Footer -->
        <tr>
          <td style="background-color: #0b1120; padding: 22px 36px; text-align: center; border-top: 1px solid rgba(56, 189, 248, 0.15);">
            <p style="margin: 0; font-size: 11px; font-weight: 600; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase;">
              NEXRAY 3D DIGITAL ATELIER &bull; ALL RIGHTS RESERVED
            </p>
            <p style="margin: 6px 0 0 0; font-size: 10px; color: #475569;">
              This transmission and attached assets are delivered under client production license.
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

print("NexRay Brand HTML email created successfully!")
