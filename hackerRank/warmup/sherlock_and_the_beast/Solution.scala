package warmup.sherlock_and_the_beast

import scala.io.Source

object Solution {
  def main(args: Array[String]) {
    for(i <- Source.stdin.getLines.drop(1).map(_.toInt)) {
      println((i to 0 by -1).find(j => j%3 == 0 && (i-j)%5 == 0) match {
        case Some(j) => "5" * j + "3" * (i-j)
        case None => -1
      })
    }
  }
}
