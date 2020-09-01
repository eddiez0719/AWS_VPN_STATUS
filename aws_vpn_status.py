import boto3
from email.message import EmailMessage
import smtplib

def a_function():
    ign = ['ourimbah - backup', 'Vineyard', 'Chatswood', 'Mandurah Coastal', 'Mandural South', 'Canberra',
           'Coast Animal Health', 'IT_Test_4G_WAN1', 'IT_Test_4G_WAN2']
    # TODO implement
    region_source = 'ap-southeast-2'
    client_resource = boto3.client('ec2', region_name=region_source)
    res = client_resource.describe_vpn_connections(
        Filters=[
            {
            }
        ]
    )
    # print(res)
    i = res["VpnConnections"]
    for l in i:
        # print(l)
        print('-------------------------')
        print('\nCGWId: {}, Clinic: {}, State: {}, Type: {}, VPNConnectionID: {}, AWS Tunnel1 IP: {}, Tunnel_1 Status: {}, AWS Tunnel2 IP: {}, Tunnel_2 Status: {}'.format(l['CustomerGatewayId'], l['Tags'][0]['Value'], l['State'], l['Type'], l['VpnConnectionId'],
                '\n' + l['VgwTelemetry'][0]['OutsideIpAddress'], l['VgwTelemetry'][0]['Status'],
                l['VgwTelemetry'][1]['OutsideIpAddress'], l['VgwTelemetry'][1]['Status']))

        if l['Tags'][0]['Value'] not in ign:

            if l['VgwTelemetry'][0]['Status'] == 'DOWN' and l['VgwTelemetry'][1]['Status'] == 'DOWN':
                print('{} VPN is Down'.format(l['Tags'][0]['Value']))

                smtpsvr = 'smtp.office365.com'
                smtpserver = smtplib.SMTP(smtpsvr, 587)

                msg = EmailMessage()
                msg['Subject'] = '{} VPN is Down'.format(l['Tags'][0]['Value'])
                msg['From'] = 'frank@vet.partners'
                msg['To'] = 'yuan.li@vet.partners', 'eddie.zhang@vet.partners', 'stephen.hunt@vet.partners'

                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.login('frank@vet.partners', 'Vetp5000')
                smtpserver.send_message(msg)
                smtpserver.close()

            else:
                pass


a_function()
