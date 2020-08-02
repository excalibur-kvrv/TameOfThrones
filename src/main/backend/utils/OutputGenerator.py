from src.main.backend.services.SoutherosRulerServiceImpl import SoutherosRulerServiceImpl
import os


class OutputGenerator:
    @staticmethod
    def read_file(input_file: str):
        file_contents = []

        with open(input_file) as file:
            for line in file:
                result = line.strip().split(" ")
                kingdom = result[0]
                message = "".join(result[i] for i in range(1, len(result)) if result[i])
                file_contents.append((kingdom, message))

        return file_contents


class ConsoleOutputGenerator(OutputGenerator):
    def generate(self, input_file: str) -> None:
        messages = self.read_file(input_file)

        southeros_ruler_service = SoutherosRulerServiceImpl()
        rulers = southeros_ruler_service.find_all_allies_for_rulers(messages)

        for ruler in rulers:
            number_of_allies = len(ruler.get_allies())
            if number_of_allies > 2:
                print(ruler, *ruler.get_allies())
            else:
                print("NONE")


class FileOutputGenerator(OutputGenerator):
    def generate(self, input_file: str) -> None:
        messages = self.read_file(input_file)

        southeros_ruler_service = SoutherosRulerServiceImpl()
        rulers = southeros_ruler_service.find_all_allies_for_rulers(messages)

        file_name = os.path.split(input_file)[-1]
        save_path = os.path.join("src", "tests", "resources", "actual-" + file_name)

        with open(save_path, "w") as file:
            for ruler in rulers:
                number_of_allies = len(ruler.get_allies())
                if number_of_allies > 2:
                    file.write(ruler.get_name() + " ")
                    for ally in ruler.get_allies():
                        file.write(ally.get_name() + " ")
                else:
                    file.write("NONE")
