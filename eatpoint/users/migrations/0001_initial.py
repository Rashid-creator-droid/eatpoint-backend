# Generated by Django 4.2.5 on 2023-10-20 17:13

from django.db import migrations, models
import phonenumber_field.modelfields
import users.usermanager


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "telephone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, unique=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=150, verbose_name="First name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=150, verbose_name="Last name"),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("client", "Клиент"),
                            ("restorateur", "Ресторатор"),
                        ],
                        max_length=20,
                        verbose_name="User`s role",
                    ),
                ),
                (
                    "confirmation_code",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        verbose_name="Confirmation code",
                    ),
                ),
                (
                    "confirm_code_send_method",
                    models.CharField(
                        choices=[
                            ("sms", "СМС"),
                            ("email", "эл. почта"),
                            ("telegram", "Телеграм"),
                            ("nothing", "не отправлять"),
                        ],
                        max_length=10,
                        verbose_name="Способ отправки кода подтверждения",
                    ),
                ),
                (
                    "is_agreement",
                    models.BooleanField(
                        default=False, verbose_name="Agreement"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Active"),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
            managers=[
                ("objects", users.usermanager.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                fields=("telephone", "email"), name="phone_email_unique"
            ),
        ),
    ]