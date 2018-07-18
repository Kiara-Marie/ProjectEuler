;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname |3 (biggest prime)|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Natural [2, inf) -> ListOfNatural
;; returns the prime factorization of n

(check-expect (prime-fac 207)(list 3 3 23))
(check-expect (prime-fac 406)(list 2 7 29))

(define (prime-fac x)
  (local [(define n0 x)

          (define (fnf n lt)   ; fnf is findnextfactor
            (if (= 0 (modulo n (+ lt 2)))
                (+ lt 2)  
                (fnf n (+ lt 2))))

          (define (fn n rsf)
            (cond [(= n 1)
                   rsf]
                  [(odd? n)
                   (fn (/ n (fnf n 1)) (cons (fnf n 1) rsf))] 
                  [else
                   (fn (/ n 2) (cons 2 rsf))]))] 
    (fn x empty))) 