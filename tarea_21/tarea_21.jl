function check_input(string)
        if !isa(tryparse(Float64, string), Number)
                println("Not a number")
                exit()
        else
                if !(0.0001 <= parse(Float64, string) <= 0.9999)
                        println("Not in range")
                        exit()
                end
        end
end

function find_prime_factors(number)
    prime_factor_array = Any[]
    while number % 2 == 0
        push!(prime_factor_array, 2)
        number /= 2
    end
    
    factor = 3
    while number != 1
        if number % factor == 0
            push!(prime_factor_array, factor)
            number /= factor
        else
            factor += 2
        end
    end
    return prime_factor_array
end

function main()
    check_input(ARGS[1])

    denominator = 10000
    numerator = Int(round(parse(Float32, ARGS[1]) * denominator, RoundNearest))
    
    denominator_prime_factor_list = find_prime_factors(denominator)
    
    for prime_factor in denominator_prime_factor_list
        if numerator % prime_factor == 0
            numerator /= prime_factor
            denominator /= prime_factor
        end
    end
    println(Int(numerator), "/", Int(denominator))
end
    
main()
