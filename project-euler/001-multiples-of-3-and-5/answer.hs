
start :: Integer
numbers :: [Integer]
end :: Integer

start = 1 :: Integer
end = 1000 :: Integer
numbers = [
    x |
    x <- [start..end],
    mod x 3 == 0 || mod x 5 == 0]
answer = sum numbers
main = print answer