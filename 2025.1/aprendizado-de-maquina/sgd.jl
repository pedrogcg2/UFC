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
    while iter < 10000
        iter += 1
        estimations = featureswithintercept * parameters
        parameters = optimizeparameters(alpha, estimations, pattern, featureswithintercept, parameters)
        println("parameters find on iteration ", iter, ": ", parameters)
    end
    return (iter, parameters)
end


function optimizeparameters(alpha::Number, estimations::Array, pattern::Array, features::Array, parameters::Array)
    size = length(estimations)
    i = rand(1:size)
    error = pattern[i] - estimations[i]
    gradient = error * features[i, :]
    return parameters + alpha * gradient
end

stochastic_gradientdescent(Float32(0.01), heights, sizes)
