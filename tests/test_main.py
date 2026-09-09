from src.personal_ai.main import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()

    assert captured.out.strip() == "Personal AI Assistant"