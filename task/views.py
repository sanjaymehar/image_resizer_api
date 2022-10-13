from io import BytesIO
from django.core.files import File
from task.models import Imagee,Eimage
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from PIL import Image, ImageOps
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class YourModelView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer
    queryset = Imagee.objects.all()

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            c=Imagee.objects.get(id=serializer.data['id'])
            image=c.image.path
         

            def gray(image):
                im = Image.open(image)
                im_io = BytesIO() 
                im=ImageOps.grayscale(im)

                im = im.save(im_io,'JPEG', quality=70, optimize=True) 

                new_image = File(im_io, name="gray.jpg")
                return new_image
            def thumb(image):
                im = Image.open(image)
                im_io = BytesIO() 

                new_width  = 200
                new_height = 300
                im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)

                im = im.save(im_io,'JPEG', quality=70, optimize=True) 

                new_image = File(im_io, name="thumbnail.jpg")
                return new_image
            def medium(image):
                im = Image.open(image)
                im_io = BytesIO() 
                new_width  = 500
                new_height = 500
                im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)

                im = im.save(im_io,'JPEG', quality=70, optimize=True) 

                new_image = File(im_io, name="medium.jpg")
                return new_image
            def large(image):
                im = Image.open(image)
                im_io = BytesIO() 

                new_width  = 1024
                new_height = 768
                im = im.resize((new_width, new_height), Image.Resampling.LANCZOS)

                im = im.save(im_io,'JPEG', quality=70, optimize=True) 

                new_image = File(im_io, name="large.jpg")
                return new_image

            a=gray(image)
            b=thumb(image)
            e=medium(image)
            d=large(image)
            z=Eimage.objects.create(orignal=c,gray=a,thumbnail=b,medium=e,large=d)
            z.save()

            ser=Eimage.objects.filter(id=z.id)
            
            serializer =ISerializer(ser, context={"request": request}, many=True)
            return Response(serializer.data)



 