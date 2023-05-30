(define (substitute s old new) 'YOUR-CODE-HERE)

; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s)
      nil
      (cons (fn (car s)) (map fn (cdr s)))))

(define (filter fn s)
  (cond 
    ((null? s)    nil)
    ((fn (car s)) (cons (car s) (filter fn (cdr s))))
    (else         (filter fn (cdr s)))))

(define (count x s) 'YOUR-CODE-HERE)

(define (unique s) 'YOUR-CODE-HERE)

(define (tally names) 'YOUR-CODE-HERE)
