package strings.palindrome_index

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    def isPalindrome(s: String) = s == s.reverse

    for(ln <- Source.stdin.getLines.drop(1)) {
      println(
        if(isPalindrome(ln)) -1
        else {
          val l = ln.length
          val i = (0 until l/2).find(i => ln(i) != ln(l-i-1)).getOrElse(-1)
          if(isPalindrome(ln.substring(0, i) + ln.substring(i+1))) i
          else l - i - 1
        }
      )
    }
  }
}
