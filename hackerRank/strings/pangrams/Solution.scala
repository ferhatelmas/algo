package strings.pangrams

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    println(
      if(Source.stdin.getLines.next
               .toLowerCase.distinct
               .diff(Seq(' ')).length == 26) "pangram"
      else "not pangram"
    )
  }
}
