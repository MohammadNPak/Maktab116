import argparse


class BaseClass:

    def __init__(self, **kwargs) -> None:
        self.name = kwargs['name']
        self.id = None

        if self.__class__.__name__ != "Tag":
            self.cpc = kwargs.get('cpc')
            self.tags = kwargs.get('tags')

        validation, message = self.validate()
        if validation:
            _, message = self.save()
        print(message)

    def validate(self):
        if not self.validate_name():
            message = f'Error: {self.__class__.__name__} already exists'
            return False, message
        elif self.__class__.__name__ != "Tag":
            if not Tag.validate_tags(self.tags):
                message = f'Error: Tag not found'
                return False, message
        return True, ''

    def validate_name(self):
        if self.name in self.objects:
            return False
        return True

    def save(self):

        self.__class__.counter += 1
        self.id = self.__class__.counter
        self.__class__.objects[self.name] = self
        message = f'Done: {self.__class__.__name__} id is {self.id}'
        return True, message

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id:{self.id},name:{self.name})"

    @classmethod
    def list(cls):
        return f"{cls.__name__.upper()}s: " + " ".join(
            [str(x) for x in sorted(cls.objects.values(), key=lambda y: y.id)])


class Suggest:
    """suggest class"""
    @classmethod
    def get(cls, index):
        for p in cls.objects.values():
            if p.id == index:
                return p
        raise IndexError(f"Error: {cls.__name__} not found")

    def suggest(self):
        def calculate(other):
            other_tags = set(other.tags)
            intersection = set(self.tags).intersection(other_tags)
            f1 = 1/max(1, other.cpc-self.cpc)
            f2 = (len(intersection)-(len(other_tags)-len(intersection)))
            return f1*f2

        ref = Ads if self.__class__.__name__ == "Place" else Place

        return f"SUGGEST-{ref.__name__.upper()}: "+" ".join(
            [str(x.id) for x in sorted(
                sorted(ref.objects.values(), key=lambda y: y.id),
                key=calculate,
                reverse=True)])


class Tag(BaseClass):
    objects = {}
    counter = 0

    @classmethod
    def validate_tags(cls, tags):
        if tags is None:
            return False
        for tag in tags:
            if tag not in cls.objects:
                return False
        return True


class Ads(BaseClass, Suggest):
    objects = {}
    counter = 0

    def validate(self):
        if not self.validate_name():
            message = f'Error: Ad already exists'
            return False, message
        elif not Tag.validate_tags(self.tags):
            message = f'Error: Tag not found'
            return False, message
        return True, ''


class Place(BaseClass, Suggest):
    objects = {}
    counter = 0


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    add_tags = subparsers.add_parser('ADD-TAG',)
    add_tags.add_argument("-name", required=True)

    tag_list = subparsers.add_parser('TAG-LIST')

    add_ads = subparsers.add_parser('ADD-ADS')
    add_ads.add_argument("-name", required=True)
    add_ads.add_argument("-cpc", required=True, type=int)
    add_ads.add_argument("-tags", nargs="*")
    ads_list = subparsers.add_parser('ADS-LIST')

    add_place = subparsers.add_parser('ADD-PLACE')
    add_place.add_argument("-name", required=True)
    add_place.add_argument("-cpc", required=True, type=int)
    add_place.add_argument("-tags", nargs="*")
    place_list = subparsers.add_parser('PLACE-LIST')

    suggest_adds = subparsers.add_parser('SUGGEST-ADS')
    suggest_adds.add_argument("-id", required=True, type=int)

    suggest_place = subparsers.add_parser('SUGGEST-PLACE')
    suggest_place.add_argument("-id", required=True, type=int)

    match = subparsers.add_parser('MATCH')
    match.add_argument("-ads-id", required=True, type=int)
    match.add_argument("-place-id", required=True, type=int)
    return parser


def main():
    n = int(input())
    parser = get_parser()
    for _ in range(n):
        req = vars(parser.parse_args(input().split()))
        command = req.pop("command")
        if command == "ADD-TAG":
            Tag(**req)
        elif command == "TAG-LIST":
            print(Tag.list())
        elif command == "ADD-ADS":
            Ads(**req)
        elif command == "ADS-LIST":
            print(Ads.list())
        elif command == "ADD-PLACE":
            Place(**req)
        elif command == "PLACE-LIST":
            print(Place.list())

        elif command == "SUGGEST-ADS":
            id = req["id"]
            try:
                p = Place.get(id)
                output = p.suggest()
                print(output)
            except IndexError as e:
                print(e)

        elif command == "SUGGEST-PLACE":
            try:
                a = Ads.get(req['id'])
                output = a.suggest()
                print(output)
            except IndexError as e:
                print(e)
        elif command == "MATCH":
            try:
                a = Ads.get(req['ads_id'])
                p = Place.get(req['place_id'])
                Ads.objects.pop(a.name)
                Place.objects.pop(p.name)
                print(f"Done: {a.id} matched to {p.id}")
            except IndexError as e:
                print(e)


if __name__ == "__main__":
    main()



# a = [2]
# refcount
# ...