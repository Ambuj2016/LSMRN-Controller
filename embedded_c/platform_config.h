// platform_config.h

#ifndef PLATFORM_CONFIG_H
#define PLATFORM_CONFIG_H

#define INPUT_SIZE 4
#define HIDDEN_SIZE 6

#define ALPHA_C 0.001f
#define BETA_C 0.9f

#define DELTA_T 0.01f  // sampling time in seconds
#define LAMBDA_1 1e-4f
#define LAMBDA_2 1e-4f
#define LAMBDA_3 1e-4f

#define SATURATION_LIMIT 0.999f

inline float sat(float x) {
    if (x > SATURATION_LIMIT) return SATURATION_LIMIT;
    if (x < -SATURATION_LIMIT) return -SATURATION_LIMIT;
    return x;
}

inline float tanh_approx(float x) {
    return (x < -3.0f) ? -1.0f : (x > 3.0f) ? 1.0f : x * (27 + x * x) / (27 + 9 * x * x);
}

inline float arctanh_approx(float y) {
    return 0.5f * logf((1 + y) / (1 - y));
}

#endif // PLATFORM_CONFIG_H
