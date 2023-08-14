from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        link_topup = request.args.get('url')  # Get the 'url' parameter from the query

        postData = {
            'do': 'confirm',
            'url': link_topup
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows 98; Win 9x 4.90) AppleWebKit/5332 (KHTML, like Gecko) Chrome/36.0.870.0 Mobile Safari/5332',
            'Host': 'www.arcshop.in.th',
        'Cookie': 'arcshop=7bkpbngo1p0qk5mi7nigs37nek8rntck; _gcl_au=1.1.1299685118.1692013478; _gid=GA1.3.1152518994.1692013479; cf_clearance=eIVAMaKxIm.j5Z8aE6fVfzjDM1Ry5rELAJrvo_yakk4-1692013482-0-1-8d136230.8eee76af.da123dd0-0.2.1692013482; twk_idm_key=it5BVBGwbQZuDXGGd0-Q1; arcshopaccount=kqODrMcgCDSKGtXPJlsxaooXiGaeyqfmWMhAEQzdHbAcdrjjtuIvwHvUNxpiVTTs; _ga_WPNMZDR72H=GS1.1.1692013478.1.1.1692013498.0.0.0; _ga=GA1.3.642151656.1692013479; _ga_30PLGWBTMP=GS1.3.1692013482.1.1.1692013499.43.0.0; TawkConnectionTime=0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.arcshop.in.th',
        'Referer': 'https://www.arcshop.in.th/topup/truewalletGift'
        }

        # Make an HTTP POST request
        with requests.Session() as session:
          response = session.post('https://www.arcshop.in.th/action/topup/truewalletGift', data=postData, headers=headers)

        # Send the HTML content received from the external server as the response
        return response.text, response.status_code
    except Exception as error:
        print('Requests Error:', error)
        return 'An error occurred while fetching the data.', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
