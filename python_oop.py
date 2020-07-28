"""
Description: Create TestRail client for generating Test Suites

Features:
- TestSuite should be created with (username list(First Name/Last Name), user_email, user_password)
- Show in test cases all user data except password (password should be shown as '********')
- Create test suite for login/registration/article create flow
- Please use the same steps in common methods
- Validate valid user email and profile

Testing:
- Run all your testsuite using calling methods for suite_object
"""


class TestRunBuilder:
    url = 'https://react-redux.realworld.io/'

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        if '@' and '.' in user_email:
            self.email = user_email
        else:
            print('Invalid email')
        if len(user_password)>=8:
            self.password = user_password
        else:
            print('The password must be at least 8 characters long')

    def login_flow(self):
        print('Click on [Sign in] button')
        print(f'Enter user email {self.user_email}')
        print(f'Enter user password {self.user_password}')
        print('Click [Sign in] button')

    def registration_suite(self):
        print('Registration')
        print('______________________________________')
        print(f'Click on [Sign up] button')
        print(f'Enter username {self.user_name}')
        print(f'Enter user email as {self.user_email}')
        print(f'Enter password as {self.user_password}')
        print('Click on [Sign up] button')

    def create_article(self):
        print('______________________________________')
        self.login_flow()
        print('Click [New article] button')
        print('Fill all fields as test data')
        print('Click [Publish] button')

    def test_run_smoke(self):
        self.login_flow()

    def test_run_sanity(self):
        self.create_article()

    def test_run_regression(self):
        self.registration_suite()
        self.login_flow()
        self.create_article()

test_run_smoke = TestRunBuilder('Hwi', 'hwi@hwi.com', '12345678')
test_run_sanity = TestRunBuilder('Sunho', 'sunho@sunho.com', '12345678')
test_run_regression = TestRunBuilder('Heejae', 'heejae@heejae.com', '12345678')

test_run_smoke.test_run_smoke()
test_run_sanity.test_run_sanity()
test_run_regression.test_run_regression()

# test_run_smoke = TestRunBuilder(username, user_email, user_password)
# test_run_sanity = TestRunBuilder(username, user_email, user_password)
# test_run_regression = TestRunBuilder(username, user_email, user_password)

