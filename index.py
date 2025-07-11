# import math

# # کلاس House برای نگه‌داری مساحت دیوار
# class House:
#     def __init__(self, wall_area):
#         self.wall_area = wall_area

# # کلاس Paint برای محاسبه تعداد سطل‌های رنگ مورد نیاز
# class Paint:
#     def __init__(self, coverage_per_bucket):
#         self.coverage_per_bucket = coverage_per_bucket

#     def calculate_buckets(self, wall_area):
#         return math.ceil(wall_area / self.coverage_per_bucket)

# # گرفتن ورودی از کاربر
# try:
#     user_input = float(input("لطفاً متراژ دیوار را به متر مربع وارد کنید: "))
#     if user_input <= 0:
#         print("لطفاً عددی بزرگ‌تر از صفر وارد کنید.")
#     else:
#         my_house = (user_input)
#         paint = Paint(10)  # هر سطل رنگ ۱۰ متر مربع را پوشش می‌دهد

#         buckets_needed = paint.calculate_buckets(my_house.wall_area)

#         print("✅ تعداد سطل‌های رنگ مورد نیاز:", buckets_needed)
# except ValueError:
#     print("لطفاً فقط عدد وارد کنید.")


# import math

# class House:
#     def __init__(self,wall_area):
#      self.wall_area=wall_area
 
# class Paint:
#      def __init__(self,cover_per_bucket):
#          self.cover_per_bucket=cover_per_bucket
         
#      def calculate_buckets(self,wall_area):
#          return math.ceil(wall_area/self.cover_per_bucket)
     
# try:
#     user_input=float(input("metrag divar ra vared konid :"))
#     if user_input <=0:
#         print("lotfan adad bozorgtar vared konid :")
#     else:
#         my_house=House(user_input)
#         paint=Paint(10)
        
#         buckets_need=paint.calculate_buckets(my_house.wall_area) 
#         print("tedad satl haye mored niyaz:",buckets_need)
# except ValueError:
#     print("lotfan faghat  adad vared konid")             
                 

# class Rectangle:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
        
#     def area(self):
#         return self.x*self.y

# rect1=Rectangle(4,5)

# print("مساحت" , rect1. area())


class House:
    def __init__(self,wall_area)
        self.wall_area=wall_area

        