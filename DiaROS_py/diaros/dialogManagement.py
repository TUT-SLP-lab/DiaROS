import requests
import json
import sys
import os
import openai

class DialogManagement:
    def __init__(self):
        # read API key
        with open(os.environ['OPENAI_APIKEY'],encoding='utf-8') as f:
            self.key = f.readline().strip()
        openai.api_key = self.key
        # self.url = "https://api.a3rt.recruit.co.jp/talk/v1/smalltalk" # エンドポイントURL
        self.rc = { "word": "" }
        sys.stdout.write('DialogManagement start up.\n')
        sys.stdout.write('=====================================================\n')

    def response(self, query):
        print(query)
        try:
            if query == "dummy":
                return "はい"
            prompt = "あなたはuserの親友です。この会話は雑談なので、あたかも実際に会話をしているような文を生成してください。また、回答は15文字以内の1文にしてください。"
            # res = requests.post( self.url, {'apikey': self.key, 'query': query } )
            chatgpt_response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages = [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": query}
                ]
                
            )
            text = chatgpt_response.choices[0].message.content
            return text # HTTPステータスコードを取得する方法がわからなかったので、別の方法でエラーハンドリングをする
            # data = res.json()
            # if data['status'] == 0:
            #     reply = data['results'][0]['reply'] # レスポンス結果
            #     return reply
            # else: # レスポンスに不備あり
            #     return f"リクエストエラー (status: {str(data['status'])}, message: {data['message']})"
        except Exception as e:
            return f"不明なエラー：{e.args}"


if __name__ == '__main__': 
    api = DialogManagement()

    while True:
        text = input('input:')
        print(f'API: {api.response(text)}')


