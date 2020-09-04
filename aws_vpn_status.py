import boto3
from email.message import EmailMessage
import smtplib

def a_function():
    ign = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i']
    # TODO implement
    region_source = 'ap-southeast-2'
    client_resource = boto3.client('ec2', region_name=region_source)
    res = client_resource.describe_vpn_connections(
        Filters=[
            {
            }
        ]
    )
    i = res
    for l in i["VpnConnections"]:
        #print(l['Tags'])
        for key in l['Tags']:
            kl = (key['Value']).lower()
            #print(kl)
            print('\nCGWId: {}, Clinic: {}, State: {}, Type: {}, VPNConnectionID: {}, AWS Tunnel1 IP: {}, Tunnel_1 Status: {}, AWS Tunnel2 IP: {}, Tunnel_2 Status: {}'.format(l['CustomerGatewayId'], kl, l['State'], l['Type'], l['VpnConnectionId'], '\n' + l['VgwTelemetry'][0]['OutsideIpAddress'], l['VgwTelemetry'][0]['Status'], l['VgwTelemetry'][1]['OutsideIpAddress'], l['VgwTelemetry'][1]['Status']))
            if kl not in ign:
                if l['VgwTelemetry'][0]['Status'] == 'DOWN' and l['VgwTelemetry'][1]['Status'] == 'DOWN':
                    print('{} VPN is Down'.format(kl))
                    
                    smtpsvr = 'smtp.office365.com'
                    smtpserver = smtplib.SMTP(smtpsvr, 587)

                    msg = EmailMessage()
                    msg['Subject'] = '{} VPN is Down'.format(kl)
                    msg['From'] = 'c@xxx.com.au'
                    msg['To'] = 'a@xxx.com.au'

                    smtpserver.ehlo()
                    smtpserver.starttls()
                    smtpserver.login('c@xxx.com.au', 'password')
                    smtpserver.send_message(msg)
                    smtpserver.close()

                else:
                    pass


a_function()

