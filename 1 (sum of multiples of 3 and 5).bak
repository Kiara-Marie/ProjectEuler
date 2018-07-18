;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |1 (sum of multiples of 3 and 5)|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))

;; Natural -> Natural
;; produces the sum of all multiples of 3 or 5 below n
(define (sum-3-5-multiples n)(sum (3-5-multiples (n-list n))))

;; Natural -> ListOfNatural
;; returns a list of all naturals up to the given one
(check-expect (n-list 5)(cons 5 (cons 4 (cons 3 (cons 2 (cons 1 (cons 0 empty)))))))

(define (n-list n)
  (cond [(zero? n) (cons 0 empty)]
        [else
         (cons n                              
               (n-list(sub1 n)))]))

;; ListOfNatural -> ListOfNatural
;; returns a list of naturals which only includes multiples of 3 and 5
(check-expect (3-5-multiples (n-list 5))(cons 5 (cons 3 (cons 0 empty))))

(define (3-5-multiples lon)
  (cond [(empty? lon)empty]
        [else
         (if (or (= 0 (modulo (first lon) 3))(= 0 (modulo (first lon) 5)))                          
             (cons (first lon)(3-5-multiples (rest lon)))
             (3-5-multiples (rest lon)))]))
;; ListOfNatural -> Natural

(define (sum lon)
  (cond [(empty? lon) 0]
        [else (+ (first lon) (sum (rest lon)))]))