heights = [1.087, 1.613, 0.953, 1.003, 1.156, 0.978, 1.092, 0.572, 0.940, 0.597, 0.838, 1.473]
sizes = [37.0; 50.0; 34.0; 36.0; 43.0; 28.0; 37.0; 20.0; 34.0; 30.0; 38.0; 47.0]

function descedentgradient(alpha::Float32, features::Array, pattern::Array)
    featuresize = size(features, 1)

    featurequantity = ndims(features) > 1 ? size(features, 2) : 1
    intercept = fill(1, featuresize)
    featureswithintercept = [features intercept]
    parameters = zeros(featurequantity + 1)
    iter = 0
    while iter < 10000
        iter += 1
        n::Integer = length(pattern)
        estimation = featureswithintercept * parameters
        parameters = optimizeparameters(alpha, estimation, parameters, featureswithintercept, pattern)
        println("parameters find on iteration ", iter, ": ", parameters)
    end
    return (iter, parameters)
end

function optimizeparameters(alpha::Float32, estimationsvec::Array, currentparams::Array, features::Matrix, patterns::Array)
    errors = patterns - estimationsvec
    gradient = features' * errors
    n = size(estimationsvec, 1)
    return currentparams + (alpha * gradient) / n
end

#MSE - mean squared error
function costfuction(pattern::Array{Float32}, patternestimation::Array{Float32})
    n = length(pattern)
    sum::float = 0
    for i in 1:n
        sum += (pattern[i] - patternestimation[i])^2
    end
    return sum / 2 * n
end

(iterationsneeded::Integer, estimations) = descedentgradient(Float32(0.1), heights, sizes)
