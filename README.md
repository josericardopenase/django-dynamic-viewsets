# Dynamic django viewsets for drf

![](https://inlab.fib.upc.edu/sites/default/files/styles/large/public/field/image/django-rest-framework.jpg)


## What are dynamic views

Dynamic views is a efficient ways of reduce your amount of serializers.This is achieved because through the viewset that django_dynamic_fields provides, the fields can be selected depending on the action that is being performed

### example:

```python
class ArticleViewSet(DynamicViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	action_fields = {
		'list' : ('id', ,'title', 'pub_date', 'excerpt'),
		'retrieve': ('id', 'title', 'pub_date', 'text', 'author'),
	}
```


## Features and advantage

- Create your own viewsets using concrete fields per action.
- Create serializers with dynamic fields
- Reusable components.
- Less amount of serializers

## Tutorial:

Start using django_dynamic_fields is so easy. First we must create our custom serializer and make it inherit  from DynamicFieldsModelSerializer.

```python
class ArticleSerializer(DynamicFieldsModelSerializer):
	class Meta:
		model = Article
		fields = '__all__'
```

Easy as that. Then we must create our custom viewset like the example before.

```python
class ArticleViewSet(DynamicViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	action_fields = {
		'list' : ('id', ,'title', 'pub_date', 'excerpt'),
		'retrieve': ('id', 'title', 'pub_date', 'text', 'author'),
	}
```
And thats all!! Happy hacking :)
