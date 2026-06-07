class ApiStatisticsService:
    def count_api_calls(self,logs):
        count_map={}
        for log in logs:
            api=log['api']
            if api in count_map:
                count_map[api]+=1
            else:
                count_map[api]=1
        result=[]
        for api,count in count_map.items():
            result.append(
                {'api':api,
                 'count':count}
            )
        return result
logs = [
    {"api": "/login"},
    {"api": "/pay"},
    {"api": "/login"},
    {"api": "/user"},
    {"api": "/pay"},
    {"api": "/login"},
]
service = ApiStatisticsService()

print(service.count_api_calls(logs),end="\n")