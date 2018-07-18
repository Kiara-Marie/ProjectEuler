;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname |4 (palindrome 3digit product)|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; String -> Boolean
;; determines if the given number is a palindrome
(check-expect (palindrome? 1) true)
(check-expect (palindrome? 25) false)
(check-expect (palindrome? 101) true)
(check-expect (palindrome? 256787652) true)

(define (palindrome? n)
  (local [(define s (if (number? n)
                        (number->string n)
                        n))]
          (cond [(> 2 (string-length s)) true]
                [else (and (string=? (substring s 0 1) (substring s (- (string-length s) 1)))
                           (palindrome? (substring s 1 (- (string-length s) 1))))])))


                                 
