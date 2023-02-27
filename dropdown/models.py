from django.db import models


class Actor(models.Model):
    name_actor = models.CharField(max_length=250, verbose_name='Актер')

    def __str__(self):
        return self.name_actor
    class Meta:
        verbose_name_plural = 'Актер'
        verbose_name = 'Актеры'






class Prepod(models.Model):
    # cat = models.ForeignKey(Category, on_delete=models.CASCADE,
    #                         verbose_name='Актер')
    name_prepod = models.CharField(max_length=250, verbose_name='Препод')

    def __str__(self):
        return self.name_prepod
    class Meta:
        verbose_name_plural = 'Преподы'
        verbose_name = 'Преподы'



class Room(models.Model):
    # subcat = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
    #                            verbose_name='Препод')
    room = models.CharField(max_length=250, verbose_name='Кабинет')
    # price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Пока хз')

    def __str__(self):
        return self.room
    class Meta:
        verbose_name_plural = 'Кабинет'
        verbose_name = 'Кабинет'




class OrderItem(models.Model):
    order = models.ForeignKey("dropdown.Order",null=True, on_delete=models.CASCADE, verbose_name="ЗАлупа")
    cat = models.ForeignKey(Actor, on_delete=models.CASCADE, verbose_name='Актер')
    subcat = models.ForeignKey(Prepod, on_delete=models.CASCADE, verbose_name='Препод')
    name_good = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Кабинет')
    time = models.CharField(null=True,max_length=20,default=0, verbose_name='Время')
    # amount = models.DecimalField(null=True,max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Актер:{self.cat}/Препод: {self.subcat}/Кабинет: {self.name_good}'



class Order(models.Model):
    date = models.DateField(null=True,verbose_name='Дата')
    # order_id = models.PositiveIntegerField(unique=True)
    # order_date = models.DateTimeField(auto_now=True)
    # total_quantity = models.PositiveIntegerField(default=0)
    # total_amount = models.DecimalField(max_digits=9, decimal_places=2)
    #
    # def __str__(self):
    #     return str(self.order_id)
    def __str__(self):
        return str(self.date)
    class Meta:
        verbose_name_plural = 'Уроки'
        verbose_name = 'Урок'

class AllowedCombination(models.Model):
    cat = models.ForeignKey(Actor, on_delete=models.CASCADE)
    subcat = models.ForeignKey(Prepod, on_delete=models.CASCADE)
    good = models.ForeignKey(Room, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.cat} {self.subcat} {self.good}'

    class Meta:
        ordering = ['pk']
        verbose_name_plural = 'Всевозможные комбинации'
        verbose_name = 'Всевозможные комбинации'


class Rep(models.Model):
    data = models.DateField(verbose_name='Дата')
    spec = models.CharField(max_length=20, verbose_name='Спектакль')
    class Meta:
        verbose_name_plural = 'Репетиция'
        verbose_name = 'Репетиция'

class RepActor(models.Model):
    order = models.ForeignKey("dropdown.Order", null=True, on_delete=models.CASCADE, verbose_name="ЗАлупа")
    cat = models.ForeignKey(Actor, on_delete=models.CASCADE, verbose_name='Актер')
    subcat = models.ForeignKey(Prepod, on_delete=models.CASCADE, verbose_name='Препод')
    name_good = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Кабинет')
    time = models.CharField(null=True, max_length=20, default=0, verbose_name='Время')

    # amount = models.DecimalField(null=True,max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Актер:{self.cat}/Препод: {self.subcat}/Кабинет: {self.name_good}'