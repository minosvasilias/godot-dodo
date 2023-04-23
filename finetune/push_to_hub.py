from dataclasses import dataclass, field
import transformers

from train import ModelArguments


@dataclass
class PushArguments:
    push_name: str = field(
        default=None,
        metadata={
            "help": "Name of huggingface model to push to."},
    )
    auth_token: str = field(
        default=None,
        metadata={
            "help": "Huggingface auth token to use."},
    )


def push():
    parser = transformers.HfArgumentParser(
        (ModelArguments, PushArguments))
    model_args, push_args = parser.parse_args_into_dataclasses()

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_args.model_name_or_path,
    )
    model.push_to_hub(push_args.push_name, use_auth_token=push_args.auth_token)


if __name__ == "__main__":
    push()
