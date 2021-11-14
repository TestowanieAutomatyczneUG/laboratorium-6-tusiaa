import unittest
from assertpy import assert_that
from Zad3 import song

class SongTest(unittest.TestCase):

    def setUp(self):
        self.temp = song()

    def test_song_all (self):
        assert_that(self.temp.write()).starts_with("On the first day of Christmas").contains("On the twelfth day of Christmas")

    def test_song_zero (self):
        assert_that(self.temp.write(0)).is_equal_to("")

    def test_song_first_line (self):
        assert_that(self.temp.write(1)).is_equal_to("On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_song_last_line (self):
        assert_that(self.temp.write(12)).starts_with("On the twelfth day of Christmas").ends_with("and a Partridge in a Pear Tree.")

    def test_song_one_line (self):
        assert_that(self.temp.write(8)).starts_with("On the eighth day of Christmas").ends_with("and a Partridge in a Pear Tree.").contains("eight Maids-a-Milking, seven Swans-a-Swimming")

    def test_song_first_three_lines (self):
        assert_that(self.temp.write(1,3)).starts_with("On the first day of Christmas").contains("gave to me: three French Hens")

    def test_song_first_three_lines_starting_with_zero (self):
        assert_that(self.temp.write(0,3)).starts_with("On the first day of Christmas").contains("gave to me: three French Hens")
    
    def test_song_three_lines (self):
        assert_that(self.temp.write(3,6)).starts_with("On the third day of Christmas").contains("gave to me: six Geese-a-Laying")

    def test_song_three_lines_reverse_order (self):
        assert_that(self.temp.write(6,3)).starts_with("On the third day of Christmas").contains("gave to me: six Geese-a-Laying")

    def test_song_ten_lines (self):
        assert_that(self.temp.write(2,11)).starts_with("On the second day of Christmas").contains("gave to me: eleven Pipers Piping")

    def test_song_one_line_float (self):
        assert_that(self.temp.write(8.0)).starts_with("On the eighth day of Christmas").ends_with("and a Partridge in a Pear Tree.").contains("eight Maids-a-Milking, seven Swans-a-Swimming")

    def test_song_one_line_string (self):
        assert_that(self.temp.write('8')).starts_with("On the eighth day of Christmas").ends_with("and a Partridge in a Pear Tree.").contains("eight Maids-a-Milking, seven Swans-a-Swimming")

    def test_song_three_lines_float (self):
        assert_that(self.temp.write(3.0,6.0)).starts_with("On the third day of Christmas").contains("gave to me: six Geese-a-Laying")

    def test_song_three_lines_string (self):
        assert_that(self.temp.write('3','6')).starts_with("On the third day of Christmas").contains("gave to me: six Geese-a-Laying")

    def test_song_exceptions_single_float(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(2.5)
    
    def test_song_exceptions_one_float(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(2, 3.5)

    def test_song_exceptions_empty_string(self):
        assert_that(self.temp.write).raises(Exception).when_called_with("")
        
    def test_song_exceptions_single_string(self):
        assert_that(self.temp.write).raises(Exception).when_called_with("song")

    def test_song_exceptions_one_string(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(3, "song")

    def test_song_exceptions_too_small(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(-3)

    def test_song_exceptions_too_big(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(13)

    def test_song_exceptions_too_small_start(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(-1,10)

    def test_song_exceptions_too_big_end(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(1,15)

    def test_song_exceptions_boolean(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(True)
        
    def test_song_exceptions_array(self):
        assert_that(self.temp.write).raises(Exception).when_called_with([1,2])

    def test_song_exceptions_object(self):
        assert_that(self.temp.write).raises(Exception).when_called_with({'a':1, 'b':2})

    def test_song_exceptions_array(self):
        assert_that(self.temp.write).raises(Exception).when_called_with([1,2])

    def test_song_exceptions_none(self):
        assert_that(self.temp.write).raises(Exception).when_called_with(None)

    def tearDown(self):
        self.temp = None 
    

if __name__ == '__main__':
    unittest.main()
