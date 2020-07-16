import scrapy

from scrapy_splash import SplashFormRequest, SplashRequest


class ExampleSpider(scrapy.Spider):
    name = 'example'

    script = '''
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(
            url='https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx',
            headers={
                'Referer': 'https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx'
            },
            endpoint='execute',
            args={
                'lua_source': self.script
            },
            callback=self.parse
        )

    def parse(self, response):
        yield SplashFormRequest.from_response(

            response,
            formid='form1',
            formdata={
                '__EVENTTARGET': "ctl00$ContentPlaceHolder1$ddlDistrict",
                '__EVENTARGUMENT': "",
                '__LASTFOCUS': "",
                '__VIEWSTATE': "/wEPDwUKLTIwNzQyOTkwOA9kFgJmD2QWAgIDD2QWIAIRDw8WAh4EVGV4dAUyPGgxPk1haGFyYXNodHJhIFBvbGljZSAtIFNlcnZpY2VzIGZvciBDaXRpemVuPC9oMT5kZAITDw8WAh8ABT88aDI+Q3JpbWUgYW5kIENyaW1pbmFsIFRyYWNraW5nIE5ldHdvcmsgYW5kIFN5c3RlbXMgKENDVE5TKTxoMj5kZAIVDw8WAh8ABSLigJxFbXBvd2VyaW5nIFBvbGljZSBUaHJvdWdoIElU4oCdZGQCFw8PFgIeCEltYWdlVXJsBRV+L0ltYWdlcy90YWJfSG9tZS5wbmcWBB4Lb25tb3VzZW92ZXIFI3RoaXMuc3JjPScuLi9JbWFnZXMvdGFiX0hvbWVSTy5wbmcnHgpvbm1vdXNlb3V0BSF0aGlzLnNyYz0nLi4vSW1hZ2VzL3RhYl9Ib21lLnBuZydkAhkPDxYCHwEFGH4vSW1hZ2VzL3RhYl9BYm91dFVzLnBuZxYEHwIFJnRoaXMuc3JjPScuLi9JbWFnZXMvdGFiX0Fib3V0VXNSTy5wbmcnHwMFJHRoaXMuc3JjPScuLi9JbWFnZXMvdGFiX0Fib3V0VXMucG5nJ2QCGw8PFgIfAQUffi9JbWFnZXMvdGFiX0NpdGl6ZW5DaGFydGVyLnBuZxYEHwIFLXRoaXMuc3JjPScuLi9JbWFnZXMvdGFiX0NpdGl6ZW5DaGFydGVyUk8ucG5nJx8DBSt0aGlzLnNyYz0nLi4vSW1hZ2VzL3RhYl9DaXRpemVuQ2hhcnRlci5wbmcnZAIdDw8WAh8BBRx+L0ltYWdlcy90YWJfQ2l0aXplbkluZm8ucG5nFgQfAgUqdGhpcy5zcmM9Jy4uL0ltYWdlcy90YWJfQ2l0aXplbkluZm9STy5wbmcnHwMFKHRoaXMuc3JjPScuLi9JbWFnZXMvdGFiX0NpdGl6ZW5JbmZvLnBuZydkAh8PDxYCHwEFKH4vSW1hZ2VzL3RhYl9PbmxpbmVTZXJ2aWNlc19FbmdfYmx1ZS5wbmcWBB8CBTJ0aGlzLnNyYz0nLi4vSW1hZ2VzL3RhYl9PbmxpbmVTZXJ2aWNlc19FbmdfUk8ucG5nJx8DBTR0aGlzLnNyYz0nLi4vSW1hZ2VzL3RhYl9PbmxpbmVTZXJ2aWNlc19FbmdfYmx1ZS5wbmcnZAIhDw8WAh8BBR9+L0ltYWdlcy90YWJfT25saW5lU2VydmljZXMucG5nFgQfAgUtdGhpcy5zcmM9Jy4uL0ltYWdlcy90YWJfT25saW5lU2VydmljZXNSTy5wbmcnHwMFK3RoaXMuc3JjPScuLi9JbWFnZXMvdGFiX09ubGluZVNlcnZpY2VzLnBuZydkAiMPZBYCAgEPZBYIAgEPZBYIAgEPZBYMAgMPDxYEHgdUb29sVGlwBRpFbnRlciBEYXRlIG9mIFJlZ2lzdHJhdGlvbh4JTWF4TGVuZ3RoZmRkAgkPFggeDERpc3BsYXlNb25leQspggFBamF4Q29udHJvbFRvb2xraXQuTWFza2VkRWRpdFNob3dTeW1ib2wsIEFqYXhDb250cm9sVG9vbGtpdCwgVmVyc2lvbj00LjEuNDA0MTIuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj0yOGYwMWIwZTg0YjZkNTNlAB4OQWNjZXB0TmVnYXRpdmULKwQAHg5JbnB1dERpcmVjdGlvbgsphgFBamF4Q29udHJvbFRvb2xraXQuTWFza2VkRWRpdElucHV0RGlyZWN0aW9uLCBBamF4Q29udHJvbFRvb2xraXQsIFZlcnNpb249NC4xLjQwNDEyLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49MjhmMDFiMGU4NGI2ZDUzZQAeCkFjY2VwdEFtUG1oZAITDw8WBB8EBRpFbnRlciBEYXRlIG9mIFJlZ2lzdHJhdGlvbh8FZmRkAhkPFggfBgsrBAAfBwsrBAAfCAsrBQAfCWhkAiEPEA8WBh4ORGF0YVZhbHVlRmllbGQFC0RJU1RSSUNUX0NEHg1EYXRhVGV4dEZpZWxkBQhESVNUUklDVB4LXyFEYXRhQm91bmRnZBAVMQZTZWxlY3QKQUhNRUROQUdBUgVBS09MQQ1BTVJBVkFUSSBDSVRZDkFNUkFWQVRJIFJVUkFMD0FVUkFOR0FCQUQgQ0lUWRBBVVJBTkdBQkFEIFJVUkFMBEJFRUQIQkhBTkRBUkESQlJJSEFOIE1VTUJBSSBDSVRZCEJVTERIQU5BCkNIQU5EUkFQVVIFREhVTEUKR0FEQ0hJUk9MSQZHT05ESUEHSElOR09MSQdKQUxHQU9OBUpBTE5BCEtPTEhBUFVSBUxBVFVSC05BR1BVUiBDSVRZDE5BR1BVUiBSVVJBTAZOQU5ERUQJTkFORFVSQkFSC05BU0hJSyBDSVRZDE5BU0hJSyBSVVJBTAtOQVZJIE1VTUJBSQlPU01BTkFCQUQHUEFMR0hBUghQQVJCSEFOSRBQSU1QUkktQ0hJTkNIV0FECVBVTkUgQ0lUWQpQVU5FIFJVUkFMBlJBSUdBRBJSQUlMV0FZIEFVUkFOR0FCQUQOUkFJTFdBWSBNVU1CQUkOUkFJTFdBWSBOQUdQVVIMUkFJTFdBWSBQVU5FCVJBVE5BR0lSSQZTQU5HTEkGU0FUQVJBClNJTkRIVURVUkcMU09MQVBVUiBDSVRZDVNPTEFQVVIgUlVSQUwKVEhBTkUgQ0lUWQtUSEFORSBSVVJBTAZXQVJESEEGV0FTSElNCFlBVkFUTUFMFTEGU2VsZWN0BTE5MzcyBTE5MzczBTE5ODQyBTE5Mzc0BTE5NDA5BTE5Mzc1BTE5Mzc3BTE5Mzc2BTE5Mzc4BTE5Mzc5BTE5MzgxBTE5MzgyBTE5NDAzBTE5ODQ1BTE5ODQ2BTE5Mzg0BTE5MzgwBTE5Mzg2BTE5NDA1BTE5Mzg3BTE5Mzg4BTE5Mzg5BTE5ODQ0BTE5NDA4BTE5MzkwBTE5ODQxBTE5MzkxBTE5MzcxBTE5MzkyBTE5ODQ3BTE5MzkzBTE5Mzk0BTE5Mzg1BTE5ODQ4BTE5NDA0BTE5NDAyBTE5MzgzBTE5Mzk1BTE5Mzk2BTE5Mzk3BTE5NDA2BTE5NDEwBTE5Mzk4BTE5Mzk5BTE5NDA3BTE5NDAwBTE5ODQzBTE5NDAxFCsDMWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cWAWZkAicPEGQQFQEGU2VsZWN0FQEGU2VsZWN0FCsDAWdkZAIDDw8WAh8ABQZTZWFyY2hkZAIFDw8WAh8ABQVDbGVhcmRkAgcPDxYCHwAFBUNsb3NlZGQCAw9kFgJmD2QWAgIDDxBkDxYBZhYBBQtWaWV3IFJlY29yZBYBZmQCCQ88KwARAgEQFgAWABYADBQrAABkAgsPDxYCHgdWaXNpYmxlZ2QWAgIBD2QWAgIFDw8WAh8ABQJHb2RkAiUPDxYCHwAFB1NpdGVNYXBkZAInDw8WAh8ABRRQb2xpY2UgVW5pdHMgV2Vic2l0ZWRkAikPDxYCHwAFC0Rpc2NsYWltZXJzZGQCKw8PFgIfAAUDRkFRZGQCLQ8PFgIfAAUKQ29udGFjdCBVc2RkAi8PDxYCHwAFBzgzNTM5NjdkZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WCAUNY3RsMDAkbG1nSG9tZQUMY3RsMDAkbG1nQWJ0BQ1jdGwwMCRsbWdDaHJ0BQ1jdGwwMCRsbWdJbmZvBQ5jdGwwMCRsbWdEd25sZAULY3RsMDAkbG1nT1MFM2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkaW1nRGF0ZU9mUmVnaXN0cmF0aW9uRnJvbQUxY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpbWdEYXRlT2ZSZWdpc3RyYXRpb25UbwUlY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRnZHZEZWFkQm9keQ9nZNLpf+Rkj2ExEsj9iyKJRIhN5Foz",
                '__VIEWSTATEGENERATOR': "6F2EA376",
                '__PREVIOUSPAGE': "6Fkypj_FbKCMscMOIEbFwiAIl-t4XMDVxhwkenT13SdXVANmcLkeKVNreNUcxzCFPd2Pxt-oh_2N7OVcM2YpQJ9h0re0OFqkn5XLvLpF1J-DFQ0h0",
                '__EVENTVALIDATION': "/wEdAFY071EZoL+Wm5kdSAghqCA9CssMeMRH46lUxWxNoH/QjR5JLHBufgCBaXKcLsIHFZg2MfFCqAQ55R5q232FZgK2qoCdmcL8o03Ga7p3SNpVviXoWLdz7AIdB4qHlFb/Ei9/1ch/aUhwAcGED/suJluf7ISsvoU9AiyuaEemMV5BBJnd8M9l/EB8CbzCs/Qj58HeW1DBXpopxThMkmM3IaEA4f83zm8GjIMpdMbZJo0bg/ou0osxK9vw1/I5QAXjT4WAelg7J4xZgxz60IVmQFQVBwFQHg/XFH9pTR8T2Gs+V8qukw1XTUYPesJgPqkOxZQh262jaQ7BxUOV7QoxeNck2w47G8rm/lqu6eH38UvMjATEI1G+tctApp1T0wcXwuNCLn3Z0VPV65eVNYp7hMU8lDrezCJH7PKOMYlCjf6maxW322Wg8dLjJ0oAXaSslqZHs1bB/7i2oDFBz4DJ85TGKEfqFutX9Sc8iba6A2UA3Jbp98jppZoyKAB…N460MRst3Ymkivnm8me7KLtZghplypPrBnBqKdsArB4XzeK7XbSYhMVY6qipQKdH6cU6XeeZcmTS57SquMwbHZEhKbKL6YxYuvZmZZF8nlCQZL4zlr//3g5nyOTFulzGhY80/Z1HbCJJ6LxQbS0yD9Thl7sm6WVjYxB23A6c0dbgG4R+nkAQKMqcH6ZVn78Nu9BSKKrOVmNjQwbSsS5vUv6MFDROG0CrK/eNGU0C14yGuWM5HkGE/DyCzIKRYuDsUr1CVxXS+jyCWdB8LwDiFJV7yxNt0d/PtikuBIdrCGbTGK/JJV58CVginDn/qsq9scauaAbl2FvBQQCQMuNszcsKvvFie32VnIgxjp9PYR0Y1JxT7s4XE1eEASLLIarsRVQGJxRqon8iLGYHzEO3PB1DG6typAyQ+VpxaMiZBUOTlCcsXDdY08Kwd7PKgvFhd/UCrh6PvV7qCAPcsiiHYjV/MyKFDCcqDP54NMr6Q8BZd/x7+HnkGOBbhYRhEI",
                'ctl00$hdnSessionIdleTime': "",
                'ctl00$hdnUserUniqueId': "",
                'ctl00$ContentPlaceHolder1$txtDateOfRegistrationFrom': "03/07/2020",
                'ctl00$ContentPlaceHolder1$meeDateOfRegistrationFrom_ClientState': "",

                'ctl00$ContentPlaceHolder1$txtDateOfRegistrationTo': "03/07/2020",
                'ctl00$ContentPlaceHolder1$meeDateOfRegistrationTo_ClientState': "",
                'ctl00$ContentPlaceHolder1$ddlDistrict': "19372",
                'ctl00$ContentPlaceHolder1$ddlPoliceStation': "Select",
                'ctl00$ContentPlaceHolder1$txtFirno': "",

                'ctl00$ContentPlaceHolder1$ucRecordView$ddlPageSize': "0",
                'ctl00$ContentPlaceHolder1$ucGridRecordView$txtPageNumber': ""
            },
            callback=(self.after_login),

        )

    def after_login(self, response):
        number = response.xpath("//*[@id='ContentPlaceHolder1_lbltotalrecord']/text").get()
        print(number)
