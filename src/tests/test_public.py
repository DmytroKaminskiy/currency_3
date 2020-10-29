from django.urls import reverse

from rate.models import ContactUs


def test_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200

def test_contact_us_get_form(client):
    url = reverse('rate:contact-us-create')
    response = client.get(url)
    assert response.status_code == 200

def test_contact_us_post_form_empty_data(client):
    url = reverse('rate:contact-us-create')
    response = client.post(url, data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['This field is required.'],
        'subject': ['This field is required.'],
        'message': ['This field is required.'],
    }

def test_contact_us_post_form_wrong_email(client):
    contact_us_initial_count = ContactUs.objects.count()
    url = reverse('rate:contact-us-create')
    data = {
        'email': 'this-is-wrong-email',
        'subject': 'Subject',
        'message': 'Message',
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Enter a valid email address.'],
    }
    assert ContactUs.objects.count() == contact_us_initial_count

def test_contact_us_post_form_correct_data(client, fake):
    contact_us_initial_count = ContactUs.objects.count()

    url = reverse('rate:contact-us-create')
    data = {
        'email': 'this-is-correct-email@mail.com',
        'subject': fake.word(),
        'message': fake.word(),
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert ContactUs.objects.count() == contact_us_initial_count + 1


def test_fixt(user_fix):
    print('fixture yields')
    print(user_fix)
