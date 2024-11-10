import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class SQLiteQueryApp {
    private Connection conn;

    public SQLiteQueryApp(Connection conny) {
        this.conn = conny;
    }

    private PSPDataOnSQLite map(ResultSet resultSet) throws SQLException {
        PSPDataOnSQLite data = new PSPDataOnSQLite();
        data.setKey(resultSet.getInt("key"));
        data.setVal(resultSet.getLong("val"));
        data.setSource(resultSet.getString("source"));
        data.setInsertTime(resultSet.getString("insert_time"));
        data.setBase(resultSet.getLong("base"));
        data.setBound(resultSet.getLong("bound"));
        return data;
    }

    public List<PSPDataOnSQLite> getListForBaseAndBound(Long base, Long bound) throws SQLException {
        List<PSPDataOnSQLite> list = new ArrayList<PSPDataOnSQLite>();
        String sql = "SELECT key, val, source, insert_time, base, bound FROM psp WHERE bound = ? and base = ?";
        try (
                PreparedStatement pstatement = conn.prepareStatement(sql)) {
            pstatement.setLong(1, bound);
            pstatement.setLong(2, base);
            ResultSet resultSet = pstatement.executeQuery();

            while (resultSet.next()) {
                list.add(map(resultSet));
            }
        }
        return list;
    }

    public List<PSPDataOnSQLite> getListForBundleAndBound(String bundle, Long bound) throws SQLException {
        List<PSPDataOnSQLite> list = new ArrayList<PSPDataOnSQLite>();
        String sql = "SELECT key, val, source, insert_time, base, bound FROM psp_base_bundles WHERE bound = ? and base = ?";
        try (
                PreparedStatement pstatement = conn.prepareStatement(sql)) {
            pstatement.setLong(1, bound);
            pstatement.setString(2, bundle);
            ResultSet resultSet = pstatement.executeQuery();

            while (resultSet.next()) {
                list.add(map(resultSet));
            }
        }
        return list;
    }
}
