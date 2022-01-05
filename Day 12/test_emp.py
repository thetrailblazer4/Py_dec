import unittest
from employee import Emp

class TestEmp(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setUpClass')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass')

	def setUp(self):
		print('setUp')
		self.emp_1 = Emp('John', 'K', 500.30)
		self.emp_2 = Emp('jane', 'M', 60000)

	def tearDown(self):
		print('tearDown')

	def test_email(self):
		self.assertEqual(self.emp_1.email, 'John.K@company.com')
		self.assertEqual(self.emp_2.email, 'jane.M@company.com')

		self.emp_1.first = 'Kate'
		self.emp_2.first = 'James'

		self.assertEqual(self.emp_1.email, 'Kate.K@company.com')
		self.assertEqual(self.emp_2.email, 'James.M@company.com')

	def test_fullname(self):

		self.assertEqual(self.emp_1.fullname, 'John K')
		self.assertEqual(self.emp_2.fullname, 'jane M')

		self.emp_1.first = 'Kate'
		self.emp_2.first = 'James'

		self.assertEqual(self.emp_1.fullname, 'Kate K')
		self.assertEqual(self.emp_2.fullname, 'James M')

	def test_apply_raise(self):

		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 520)
		self.assertEqual(self.emp_2.pay, 62400)


if __name__ == '__main__':
	unittest.main()