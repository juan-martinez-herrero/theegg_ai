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

function main()
    check_input(ARGS[1])

    denominator = 10000
    numerator = Int(round(parse(Float32, ARGS[1]) * denominator, RoundNearest))

    # Hallar el máximo común divisor
    mcd = gcd(numerator, denominator)

    println(Int(numerator/mcd), '/', Int(denominator/mcd))

    end

main()
