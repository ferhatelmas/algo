class ToastXRaspberry:
    def apply(self, upper_limit, layer_count):
        return layer_count // upper_limit + (layer_count%upper_limit != 0)
