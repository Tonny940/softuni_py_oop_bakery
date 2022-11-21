class Validator:
    @staticmethod
    def validator_for_empty_string(text, message):
        if text.strip() == "":
            raise ValueError(message)

    @staticmethod
    def validate_value_equal_or_below_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_not_in_range(min_value, max_value, value, message):
        if value < min_value or max_value < value:
            raise ValueError(message)
