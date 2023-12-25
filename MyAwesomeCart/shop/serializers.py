# from rest_framework import serializers
# from shop.models import Product
# class Serializers(serializers.Serializer):
#     product_name = serializers.CharField(max_length=50)
#     category = serializers.CharField(max_length=50, default="")
#     subcategory = serializers.CharField(max_length=50, default="")

#     def create(self, validated_data):
#         return Product.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.product_name = validated_data.get('product_name', instance.product_name)
#         instance.category = validated_data.get('category', instance.category)
#         instance.subcategory  = validated_data.get('subcategory ', instance.subcategory )
#         return instance
class SupportListAPI(APIView):
    def get(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "something went worng"
        try:
            SupportRequests = SupportRequest.objects.all()
            payload = []
            for SupportRequests in SupportRequests:
                payload.append({
                    'title ': SupportRequests.title,
                    'department':SupportRequests.department,
                    'description': SupportRequests.description,
                    ' priority ': SupportRequests. priority,
                    'category ': SupportRequests.category,
                    'status': SupportRequests.status,


                })
                response['status'] = 200
                response['message'] = 'All data'
                response['data'] = payload
        except Exception as e:
            print(e)

        return Response(response)


SupportListAPI = SupportListAPI.as_view()
