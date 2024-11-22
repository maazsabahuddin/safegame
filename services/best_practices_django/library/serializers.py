# Rest framework Imports
from rest_framework import serializers

# Local Imports
from library.models.libray_model import Author, Tag, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')  # For author name as string input
    tags = serializers.ListField(child=serializers.CharField(), write_only=True)  # Accept tags as input
    tags_output = serializers.SerializerMethodField()  # For output only

    class Meta:
        model = Book
        fields = ['title', 'author', 'tags', 'tags_output']
        extra_kwargs = {
            'tags': {'write_only': True},        # Only used for input
            'tags_output': {'read_only': True}   # Only used for output
        }

    def get_tags_output(self, obj):
        """Custom method for outputting tags."""
        return [tag.name for tag in obj.tags.all()]

    def create(self, validated_data):
        # Extract the author name
        author_name = validated_data.pop('author')['name']
        author, _ = Author.objects.get_or_create(name=author_name)

        # Extract tag names
        tag_names = validated_data.pop('tags')

        # Get or create tags
        tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]

        # Create the book instance
        book = Book.objects.create(author=author, title=validated_data['title'])

        # Associate tags with the book
        book.tags.set(tags)

        return book
