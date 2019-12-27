import parser
import sys
import logging
import builder

# small example
if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(name)s] %(message)s',
        level=logging.INFO
    )
    json = (builder.JsonBuilder().
            start_object().
                start_array("array").
                    put(2).
                    start_object().
                        put("oare", "merge").
                        start_object("nested").
                            start_array("nestedArray").
                            put("some value").
                            end_array().
                        end_object().
                    end_object().
                end_array().
            end_object())

    with open("dump.json", "w") as f:
        f.write(json.build())