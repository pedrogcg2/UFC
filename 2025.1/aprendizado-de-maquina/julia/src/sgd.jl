using Plots
heights = [1.087, 1.613, 0.953, 1.003, 1.156, 0.978, 1.092, 0.572, 0.940, 0.597, 0.838, 1.473]
sizes = [37.0; 50.0; 34.0; 36.0; 43.0; 28.0; 37.0; 20.0; 34.0; 30.0; 38.0; 47.0]

function stochastic_gradientdescent(alpha::Number, features::Array, pattern::Array)
    featuresdims = ndims(features)
    featuressize = size(features, 1)
    featuresquantity = featuresdims > 1 ? size(features, 2) : 1

    intercept = ones(featuressize)
    featureswithintercept = [features intercept]

    parameters = zeros(featuresquantity + 1)
    iter = 0
    epoch = [i for i in 1:10000]
    mseperepoch = []
    while iter < 10000
        iter += 1
        estimations = featureswithintercept * parameters
        parameters = optimizeparameters(alpha, estimations, pattern, featureswithintercept, parameters)
        mse = costfuction(pattern, estimations)
        push!(mseperepoch, mse)
        println("parameters find on iteration ", iter, ": ", parameters)
    end
    return (epoch, mseperepoch, parameters)
end


function optimizeparameters(alpha::Number, estimations::Array, pattern::Array, features::Array, parameters::Array)
    size = length(estimations)
    i = rand(1:size)
    error = pattern[i] - estimations[i]
    gradient = error * features[i, :]
    return parameters + alpha * gradient
end

#MSE - mean squared error
function costfuction(pattern::Array{Float64}, patternestimation::Array{Float64})
    n = length(pattern)
    sum::Float64 = 0
    for i in 1:n
        sum += (pattern[i] - patternestimation[i])^2
    end
    return sum / 2 * n
end

(epoch, mseperepoch, parameters) = stochastic_gradientdescent(Float32(0.01), heights, sizes)
//todo: create a helper functions to display this on terminal
plt = plot(epoch, mseperepoch)
