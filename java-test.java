import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

class Student {
    private String name;
    private List<Double> scores;

    public Student(String name, List<Double> scores) {
        this.name = name;
        this.scores = scores;
    }

    public String getName() {
        return name;
    }

    public double averageScore() {
        if (scores.isEmpty()) {
            return 0;
        }
        double sum = 0;
        for (double score : scores) {
            sum += score;
        }
        return sum / scores.size();
    }
}

public class StudentReport {

    public static List<Student> readStudentsFromCSV(String filePath) {
        List<Student> students = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            br.readLine();
            while ((line = br.readLine()) != null) {
                String[] data = line.split(",");
                String name = data[0];
                List<Double> scores = new ArrayList<>();
                for (int i = 1; i < data.length; i++) {
                    scores.add(Double.parseDouble(data[i]));
                }
                students.add(new Student(name, scores));
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return students;
    }

    public static List<String> generateReport(List<Student> students) {
        List<String> reportLines = new ArrayList<>();
        reportLines.add("Student Name, Average Score");
        for (Student student : students) {
            reportLines.add(student.getName() + ", " + String.format("%.2f", student.averageScore()));
        }
        return reportLines;
    }

    public static void saveReportToFile(List<String> reportLines, String outputFile) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(outputFile))) {
            for (String line : reportLines) {
                bw.write(line);
                bw.newLine();
            }
            System.out.println("Report saved to " + outputFile);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String inputFile = "students_scores.csv";
        String outputFile = "students_report.csv";

        List<Student> students = readStudentsFromCSV(inputFile);
        List<String> reportLines = generateReport(students);
        saveReportToFile(reportLines, outputFile);
    }
}
