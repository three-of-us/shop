from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.models import Product,Category
from products.serializers import ProductSerializer, CategorySerializer
from rest_framework.generics import ListAPIView



class ProductList(ListCreateAPIView):
    '''
    getting a list of products and creating a new post
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    '''
    get, update and delete a post
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryList(ListCreateAPIView):
    '''
    getting a list of categories and creating a new post
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetail(RetrieveUpdateDestroyAPIView):
    '''
    get, update and delete a post
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductListByCategory(ListAPIView):
    '''
    list of products by category
    '''
    permission_classes= [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug)
    
class ProductListByPrice(ListAPIView):
    '''
    list of products by price
    '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def get_queryset(self):
        min_price = self.kwargs['min_price']
        max_price = self.kwargs['max_price']
        return Product.objects.filter(price__range=(min_price, max_price))